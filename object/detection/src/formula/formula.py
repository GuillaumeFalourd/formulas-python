#!/usr/bin/python3
from imageai.Detection import ObjectDetection
import os

def run(image_path):
    print("PATH:", image_path)
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    #detector.setModelPath( os.path.join(execution_path , "images/keanu_reeves.jpg"))
    detector.setModelPath("images/keanu_reeves.jpg")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
