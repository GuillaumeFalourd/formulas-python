#!/usr/bin/python3
import os

from formula import formula

sender_email = os.environ.get("RIT_SENDER_EMAIL")
sender_password = os.environ.get("RIT_SENDER_PASSWORD")
receiver_email = os.environ.get("RIT_RECEIVER_EMAIL")
subject = os.environ.get("RIT_EMAIL_SUBJECT")
message = os.environ.get("RIT_EMAIL_MESSAGE")

formula.run(sender_email, sender_password, receiver_email, subject, message)
