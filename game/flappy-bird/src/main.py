#!/usr/bin/python3
import os

from formula import formula

difficulty = os.environ.get("RIT_DIFFICULTY")

formula.run(difficulty)
