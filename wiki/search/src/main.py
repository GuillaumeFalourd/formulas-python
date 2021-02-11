#!/usr/bin/python3
import os

from formula import formula

keywords = os.environ.get("RIT_KEYWORDS")
language = os.environ.get("RIT_LANGUAGE")

formula.run(keywords, language)
