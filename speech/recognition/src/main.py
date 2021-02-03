#!/usr/bin/python3
import os

from formula import formula

txt_file = os.environ.get("TXT_FILE")
file_name = os.environ.get("FILE_NAME")

formula.run(txt_file, file_name)
