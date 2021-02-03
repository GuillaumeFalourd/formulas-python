#!/usr/bin/python3
import speech_recognition as sr
import inquirer
import re

regex_pattern_1 = "(?=`)(.*)"
regex_pattern_2 = "[0-9]"

def run(txt_file, file_name):

    device = get_microphone_device()

    text = get_speech(device)

    if text is not None and txt_file == "yes":
        create_txt_file(text, file_name)

# Identify the microphone device to use
def get_microphone_device():
    microphone_list = []
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        microphone_list.append("Microphone {1} `(device_index={0})`".format(index, name))

    questions = [
    inquirer.List('microphone',
                message = "What Microphone will you use?",
                choices = microphone_list,
            ),
    ]
    answers = inquirer.prompt(questions)
    microphone = answers["microphone"]
    microphone = re.search(regex_pattern_1, microphone).group(0)
    device = re.search(regex_pattern_2, microphone).group()

    return device

# Listen to the speaker through the microphone device
def get_speech(device):
    rec = sr.Recognizer()
    with sr.Microphone(device_index=int(device)) as source:
        print("Speak, we are listening:")
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            print("You said: \"{}\"".format(text))
        except:
            print("Sorry, the formula couldn't recognize what you said")

    return text

# Create TXT filename from text variable
def create_txt_file(text, file_name):
    with open(file_name, "w") as file:
        file.write(text)
    print("{} file created".format(file_name))