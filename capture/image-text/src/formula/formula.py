#!/usr/bin/python3
from PIL import Image
import pytesseract
# import pygame
# import pygame.camera as camera 

import pathlib
import cv2
import os
import time
import re

def run():
    
    ######## TEST 1
    
    # try:
    #     output = os.popen("which tesseract").read()
    #     tesseract_match = re.match("(.*?)(?=\\n)", output)
    #     tesseract_path = tesseract_match.group(1)
    #     pytesseract.pytesseract.tesseract_cmd = tesseract_path
    # except:
    #     print("You don't seem to have Tesseract installed. Have a look here: https://tesseract-ocr.github.io/tessdoc/Downloads.html")        


    # print("Capturing the image...")
    # time.sleep(2)
    # cap = cv2.VideoCapture(0)
    
    # while cap.isOpened():
        
    #     ret, frame = cap.read()
        
    #     if ret:
    #         captured_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         cv2.imshow('frame', captured_image)
    #         cv2.imwrite("image.jpg", captured_image)
    #         path = pathlib.Path().absolute()
        
    #         #text = pytesseract.image_to_string(Image.fromarray(captured_image))
    #         text = pytesseract.image_to_string(Image.open("{}/image.jpg".format(path)))

    #         print("Extracted Text: ", text)
                
    #         if cv2.waitKey(0) & 0xFF == ord('q'):
    #             return None
        
    #     else:
    #         raise ValueError("Can't read frame")
    
    # cap.release()
    
    ######## TEST 2
    
    # cam = cv2.VideoCapture(0)

    # cv2.namedWindow("test")

    # img_counter = 0

    # while True:
    #     ret, frame = cam.read()
    #     if not ret:
    #         print("failed to grab frame")
    #         break
    #     cv2.imshow("test", frame)

    #     k = cv2.waitKey(1)
    #     if k%256 == 27:
    #         # ESC pressed
    #         print("Escape hit, closing...")
    #         break
    #     elif k%256 == 32:
    #         # SPACE pressed
    #         img_name = "opencv_frame_{}.png".format(img_counter)
    #         cv2.imwrite(img_name, frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1

    # cam.release()

    # cv2.destroyAllWindows()
    
    # camera.init()
    # camera.list_cameras() #Camera detected or not
    # cam = camera.Camera("/dev/video0",(640,480))
    # cam.start()
    # img = cam.get_image()
    # pygame.image.save(img,"filename.jpg")

    # text = pytesseract.image_to_string(Image.fromarray(img))

    # print("Extracted Text: ", text)
    
    ######## TEST 3 
    
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        cv2.namedWindow("cam-test")
        cv2.imshow("cam-test",img)
        # cv2.waitKey(0)
        time.sleep(3)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("image.jpg",img)
        cam.release()
        
        text = pytesseract.image_to_string(Image.fromarray(img))

        print("Extracted Text: ", text)