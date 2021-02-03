# Ritchie Formula

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
- the language to convert (currently en, fr and pt).
- the audio filename that will be created where the formula is executed.
