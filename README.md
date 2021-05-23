[![Security Pipeline](https://github.com/GuillaumeFalourd/formulas-python/actions/workflows/security_pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/formulas-python/actions/workflows/security_pipeline.yml)

# Formulas Python

<img width="950" alt="title" src="https://user-images.githubusercontent.com/22433243/117589577-bdf50580-b100-11eb-9c02-5ba95ab35d89.png">

## 📚 Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)

## 🔎 What you'll find in this repository

![Image](/docs/img/rit-face-recognition-custom-with-keanu-reeves.png)

![Image](/docs/img/rit-detect-text-on-video-webcam.png)

### Recognition / Detection

- [Convert Text to Audio](https://github.com/GuillaumeFalourd/formulas-python/tree/master/convert/text-to-audio): `rit convert text-to-audio`

_Formula allowing to convert a text (from a txt file or input) to an audio file._

- [Face Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/face/recognition): `rit face recognition`

_Formula using face recognition using the computer webcam._

- [Speech Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/speech/recognition): `rit speech recognition`

_Formula using speech recognition converting what you speak in a txt file._

- [Image Text Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/detect/text-on-image): `rit detect image-to-text`

_Formula detecting text from an image input._

- [Live Text Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/detect/text-on-video): `rit detect text-on-video`

_Formula detecting text using the computer webcam._

### Others

- [Aws boto3](https://github.com/GuillaumeFalourd/formulas-python/tree/master/aws/boto3): `rit aws boto3`

_Formula using the boto3 library to interact with AWS._

- [Send Email](https://github.com/GuillaumeFalourd/formulas-python/tree/master/send/email): `rit send email`

_Formula sending an email._

- [Wikipedia Search](https://github.com/GuillaumeFalourd/formulas-python/tree/master/wiki/search): `rit wiki search`

_Formula making a wiki search based on user input._

### Working On

- [Linkedin web-scraping](https://github.com/GuillaumeFalourd/formulas-python/tree/master/linkedin/web-scraping): `rit linkedin web-scraping`
- [Object Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/object/detection): `rit object detection`

## 📦 Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/install-cli)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal (since CLI version 2.8.0):

```bash
rit add repo --provider="Github" --name="formulas-python" --repoUrl="https://github.com/GuillaumeFalourd/formulas-python" --priority=1
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.

## ♻️ Contribute to the repository

### 🆕 Creating formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Check the step by step of [how to create formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-create-formulas)
4. Add your formulas to the repository
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

### 🆒 Updating Formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Add the cloned repository to your workspaces (`rit add workspace`) with a highest priority (for example: 1).
4. Check the step by step of [how to implement formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-implement-a-formula)
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

- [Contribute to Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md)

## Similar contents

If you want to see similar formulas repositories:

- [formulas-aws](https://github.com/GuillaumeFalourd/formulas-aws): Repository with formulas interacting with AWS.

<img width="953" alt="title" src="https://user-images.githubusercontent.com/22433243/117589694-889ce780-b101-11eb-84fa-b197d0b72ee8.png">

- [formulas-insights](https://github.com/GuillaumeFalourd/formulas-insights): Repository with formulas getting insights from Github, LinkedIn, Google accounts.

![title](https://user-images.githubusercontent.com/22433243/119176109-11d8e600-ba41-11eb-8ed7-c917ab061e56.png)

- [formulas-games](https://github.com/GuillaumeFalourd/formulas-games): Repository with formulas games (pacman, space invasion)

![title](https://user-images.githubusercontent.com/22433243/119173001-fd92ea00-ba3c-11eb-9314-bad231c0bbc3.png)
