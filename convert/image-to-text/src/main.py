#!/usr/bin/python3
import os

from formula import formula

image_path = os.environ.get("RIT_IMAGE_PATH")
language = os.environ.get("RIT_IMAGE_LANGUAGE")

formula.run(image_path, language)
