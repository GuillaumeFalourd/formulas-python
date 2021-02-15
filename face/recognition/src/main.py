#!/usr/bin/python3
import os

from formula import formula

sample_picture = os.environ.get("RIT_SAMPLE_PICTURE")
image_path = os.environ.get("RIT_IMAGE_PATH")
face_name = os.environ.get("RIT_FACE_NAME")

formula.run(sample_picture, image_path, face_name)
