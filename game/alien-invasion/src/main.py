#!/usr/bin/python3
import os

from formula import formula

mode = os.environ.get("RIT_MODE")

formula.run(mode)
