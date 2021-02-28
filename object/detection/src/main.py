#!/usr/bin/python3
import os

from formula import formula

image_path = os.environ.get("RIT_IMAGE_PATH")

formula.run(image_path)
