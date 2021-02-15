#!/usr/bin/python3
import os
import json

def run(detection_type, image_path):

    if detection_type == "Image":
        input_flag_cmd = 'rit detect text-on-image --rit_image_path={}'.format(image_path)

    else:
        input_flag_cmd = 'rit detect text-on-video'

    os.system(f'{input_flag_cmd}')
