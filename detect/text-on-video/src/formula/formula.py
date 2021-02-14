#!/usr/bin/python3
from PIL import Image
from imutils.video import VideoStream
from imutils.video import FPS
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import imutils
import time
import cv2
import pytesseract
from pytesseract import Output
import os
import re

def run():

    # Check if Tesseract is installed on the computer
    try:
        output = os.popen("which tesseract").read()
        tesseract_match = re.match("(.*?)(?=\\n)", output)
        tesseract_path = tesseract_match.group(1)
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    except:
        print("You don't seem to have Tesseract installed. Have a look here: https://tesseract-ocr.github.io/tessdoc/Downloads.html")        

    # Set window and lecture configurations
    configs = [
        ("min_confidence", 0.3),
        ("width", 288),
        ("height", 288),
        ("east", "frozen_east_text_detection.pb"),
    ]

    args = {k: v for k, v in configs}

    # Initialize the original frame dimensions, the new frame dimensions and the ratio between the dimensions
    (W, H) = (None, None)
    (newW, newH) = (args["width"], args["height"])
    (rW, rH) = (None, None)

    # Define the two output layer names for the EAST detector model that we are interested:
    # The first is the output probabilities
    # The second can be used to derive the bounding box coordinates of text
    layerNames = [
        "feature_fusion/Conv_7/Sigmoid",
        "feature_fusion/concat_3"]

    # Load the pre-trained EAST text detector
    print("[INFO] loading EAST text detector...")
    net = cv2.dnn.readNet(args["east"])

    # Grab the reference to the webcam
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(1.0)

    # Start the FPS throughput estimator
    fps = FPS().start()

    fn = 0 # Frame number
    # Loop over frames from the video stream
    while True:
        # Grab the current frame
        frame = vs.read()

        # Check to see if we have reached the end of the stream
        if frame is None:
            break

        # Resize the frame, maintaining the aspect ratio
        frame = imutils.resize(frame, width=1000)
        orig = frame.copy()

        # If our frame dimensions are None
        # We still need to compute the ratio of old frame dimensions to new frame dimensions
        if W is None or H is None:
            (H, W) = frame.shape[:2]
            rW = W / float(newW)
            rH = H / float(newH)

        # Resize the frame, this time ignoring aspect ratio
        frame = cv2.resize(frame, (newW, newH))

        # Construct a blob from the frame and then perform a forward pass
        # of the model to obtain the two output layer sets
        blob = cv2.dnn.blobFromImage(
            frame,
            1.0,
            (newW, newH),
            (123.68, 116.78, 103.94),
            swapRB=True,
            crop=False
        )
        net.setInput(blob)
        (scores, geometry) = net.forward(layerNames)

        # Decode the predictions, then  apply non-maxima suppression to
        # suppress weak, overlapping bounding boxes
        (rects, confidences) = decode_predictions(scores, geometry, args)
        boxes = non_max_suppression(np.array(rects), probs=confidences)

        # Loop over the bounding boxes
        for (startX, startY, endX, endY) in boxes:
            # Scale the bounding box coordinates based on the respective ratios
            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)

            # Draw the bounding box on the frame
            cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

        # Update the FPS counter
        fps.update()

        # Show the output frame on screen
        cv2.imshow("Text Detection", orig)

        # Print extracted text from the frame if at least 3 characters are identified
        pwd = os.getcwd()
        cv2.imwrite("{}/image.jpg".format(pwd), get_grayscale(orig))
        try:
            fn += 1
            text = pytesseract.image_to_string(Image.open("{}/image.jpg".format(pwd)), lang = "eng")
            val = re.search('[a-zA-Z]{3,}',text)
            if val[0].isalpha():
                print("\033[1m✅ Extracted Text ({})\033[0m".format(fn))
                print(text)
        except:
            pass

        key = cv2.waitKey(1) & 0xFF

        # Break the loop if the `q` key is pressed on output frame screen
        if key == ord("q"):
            break

    # Stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # Release the webcam pointer
    vs.stop()

    # Close all windows
    cv2.destroyAllWindows()

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def decode_predictions(scores, geometry, args):
	# Grab the number of rows and columns from the scores volume, then initialize
    # a set of bounding box rectangles and corresponding confidence scores
	(numRows, numCols) = scores.shape[2:4]
	rects = []
	confidences = []

	# Loop over the number of rows
	for y in range(0, numRows):
		# Extract the scores (probabilities), followed by the geometrical data
        # used to derive potential bounding box coordinates that surround text
		scoresData = scores[0, 0, y]
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y]

		# Loop over the number of columns
		for x in range(0, numCols):
			# If the score does not have sufficient probability, ignore it
			if scoresData[x] < args["min_confidence"]:
				continue

			# Compute the offset factor as our resulting feature maps will be 4x smaller than the input image
			(offsetX, offsetY) = (x * 4.0, y * 4.0)

			# Extract the rotation angle for the prediction andthen compute the sin and cosine
			angle = anglesData[x]
			cos = np.cos(angle)
			sin = np.sin(angle)

			# Use the geometry volume to derive the width and height of the bounding box
			h = xData0[x] + xData2[x]
			w = xData1[x] + xData3[x]

			# Compute both the starting and ending (x, y)-coordinates for the text prediction bounding box
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h)

			# Add the bounding box coordinates and probability score to our respective lists
			rects.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])

	# Return a tuple of the bounding boxes and associated confidences
	return (rects, confidences)