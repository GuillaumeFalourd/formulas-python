#!/usr/bin/python3
import os

from formula import formula

email = os.environ.get("RIT_STACKOVERFLOW_EMAIL")
password = os.environ.get("RIT_STACKOVERFLOW_PASSWORD")
display_name = os.environ.get("RIT_STACKOVERFLOW_DISPLAY_NAME")

formula.run(email, password, display_name)
