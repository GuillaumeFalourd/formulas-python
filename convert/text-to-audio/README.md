# Ritchie Text to Audio Formula

![Execution](/docs/img/text-to-audio-python.png)

## Premisses

`Linux`: mpg321 installed using `apt-get install mpg321`

`MacOS` : None

`Windows` : None

## Command

```bash
rit convert text-to-audio
```

```bash
rit convert text-to-audio --docker
```

## Description

This formula allows the user to convert a text in audio (mp3 format) using GTTS (Google Text-to-Speech) module.

It contains at least 3 inputs:

- the text to convert (from a TXT file or typing some text).
- the language to convert (currently EN, FR and PT).
- the audio filename that will be created on the folder where the formula is executed.

## Sample

![Execution](/docs/img/rit-convert-text-to-audio.png)
