#!/usr/bin/python3
import os
import imageai

def run(image_path):
    print("PATH:", image_path)
    execution_path = os.getcwd()

    detector = imageai.Detection.ObjectDetection()
    detector.setModelTypeAsRetinaNet()

    # Test
    detector.setModelPath("images/keanu_reeves.jpg")
    #detector.setModelPath( os.path.join(execution_path , "images/keanu_reeves.jpg"))

    # Load model on an image.jpg file
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
