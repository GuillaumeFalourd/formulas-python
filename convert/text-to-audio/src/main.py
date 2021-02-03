#!/usr/bin/python3
import os

from formula import formula

exist = os.environ.get("EXIST")
file_path = os.environ.get("FILE_PATH")
file_name = os.environ.get("FILE_NAME")
text_to_convert = os.environ.get("TEXT_TO_CONVERT")
file_language = os.environ.get("FILE_LANGUAGE")
audio_file_name = os.environ.get("AUDIO_FILE_NAME")

formula.Run(exist, file_path, file_name, text_to_convert, file_language, audio_file_name)
