#!/usr/bin/python3
import os

from formula import formula

frequency = os.environ.get("RIT_FRAME_FREQUENCY")
amount = os.environ.get("RIT_AMOUNT_FREQUENCY")

formula.run(frequency, amount)
