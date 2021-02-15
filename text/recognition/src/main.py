#!/usr/bin/python3
import os

from formula import formula

detection_type = os.environ.get("RIT_DETECTION_TYPE")
image_path = os.environ.get("RIT_IMAGE_PATH")

formula.run(detection_type, image_path)
