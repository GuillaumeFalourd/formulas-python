#!/usr/bin/python3
from PIL import Image
import pytesseract
import os
import re

# List of available languages
# print(pytesseract.get_languages(config=''))

def run(image_path, language):
    try:
        output = os.popen("which tesseract").read()
        tesseract_match = re.match("(.*?)(?=\\n)", output)
        tesseract_path = tesseract_match.group(1)
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    except:
        print("You don't seem to have Tesseract installed. Have a look here: https://tesseract-ocr.github.io/tessdoc/Downloads.html")

    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang = language)
        print("\033[1m✅ Successfully convert the image into text:\033[0m")
        print(text)
    except:
        print("\033[1m❌ Error converting the image into text:\033[0m")
        print("Please, check the image path and try again.")
        print("If the problem persists, open an ISSUE on https://github.com/GuillaumeFalourd/formulas-python")
