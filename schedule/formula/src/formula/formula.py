#!/usr/bin/python3
import os
import schedule
import time

def job_function():
    print("\nJob function executing the RIT DEMO HELLO-WORLD formula")
    os.system("rit demo hello-world --rit_input_text=Dennis --rit_input_boolean=true --rit_input_list=everything --rit_input_password=Ritchie")

def run(frequency, amount):
    
    if frequency == "seconds":
        schedule.every(int(amount)).seconds.do(job_function)
        
    elif frequency == "minutes":
        schedule.every(int(amount)).minutes.do(job_function)
        
    elif frequency == "hours":
        schedule.every(int(amount)).minutes.do(job_function)
        
    else:
        print("Unexpected frequency selected")

    while 1:
        schedule.run_pending()
        time.sleep(1)
