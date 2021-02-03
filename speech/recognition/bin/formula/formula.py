#!/usr/bin/python3
import speech_recognition as sr
import inquirer
import re

regex_pattern_1 = "(?=`)(.*)"
regex_pattern_2 = "[0-9]"

def Run(txt_file, file_name):

    # Identify the microphone device to use
    device = identify_microphone_device()

    # Listen to the speaker through the microphone device
    text = get_speech(device)

    # Create TXT file from text variable
    if text is not None and txt_file == "yes":
        with open(file_name, "w") as file:
            file.write(text)
        print("{} file created".format(file_name))

def identify_microphone_device():
    microphone_list = []
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        microphone_list.append("Microphone {1} found for `Microphone(device_index={0})`".format(index, name))

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

def get_speech(device):
    r = sr.Recognizer()
    with sr.Microphone(device_index=int(device)) as source:
        print("Speak, we are listening:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: \"{}\"".format(text))
        except:
            print("Sorry could not recognize what you said")

    return text