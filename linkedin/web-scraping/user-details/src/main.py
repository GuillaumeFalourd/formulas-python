#!/usr/bin/python3
import os
import re

from formula import formula

email = os.environ.get("LINKEDIN_EMAIL")
password = os.environ.get("LINKEDIN_PASSWORD")
profiles = os.environ.get("RIT_PROFILES")
names = profiles.split('|')
path = os.environ.get("RIT_PATH")

formula.run(email, password, names, path)
