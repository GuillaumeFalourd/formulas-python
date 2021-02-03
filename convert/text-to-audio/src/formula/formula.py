#!/usr/bin/python3
from gtts import gTTS
import os
import platform

def run(exist, file_path, file_name, text_to_convert, file_language, audio_file_name):

    system = platform.system()

    if exist == "yes":
        print("Converting txt file to audio...")

        # Go inside the folder where the txt file is located
        os.chdir(file_path)

        # Open the text file
        file = open(file_name)
        text_to_convert = file.read().replace("\n", "")
        file.close()

        # Convert the text to audio
        ttmp3 = gTTS(text=text_to_convert, lang=file_language, slow=False)

        # Create the audio file in mp3 format
        filename = create_file(system, ttmp3, audio_file_name)

        # Play your audio file according to OS
        play_audio(system, filename)

    elif exist == "no":
        print("Converting input text to audio...")

        # Convert the text to audio
        ttmp3 = gTTS(text=text_to_convert, lang=file_language, slow=False)

        # Create the audio file in mp3 format
        filename = create_file(system, ttmp3, audio_file_name)

        # Play your audio file according to OS
        play_audio(system, filename)

    else:
        print("Unexpected Error, please check your inputs.")

def create_file(system, ttmp3, audio_file_name):
    if "Windows" in system:
        dirname = os.path.split(__file__)
        filename = dirname[0] + "\\" + audio_file_name + ".mp3"
    else:
        filename = audio_file_name + ".mp3"

    print("Saving audio file")
    ttmp3.save(filename)

    return filename

def play_audio(system, filename):
    # Play your audio file according to OS

    if "Darwin" in system:
        cmd = "afplay " + filename

    elif "Linux" in system:
        cmd = "mpg321 " + filename

    elif "Windows" in system:
        cmd = filename

    print("Playing audio file", filename)
    os.system(cmd)