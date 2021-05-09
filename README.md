[![Security Pipeline](https://github.com/GuillaumeFalourd/formulas-python/actions/workflows/security_pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/formulas-python/actions/workflows/security_pipeline.yml)

# Ritchie Formulas Python

<img width="950" alt="title" src="https://user-images.githubusercontent.com/22433243/117589577-bdf50580-b100-11eb-9c02-5ba95ab35d89.png">

## Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)

## Formulas available on this repository

### Done / To improve

- [Convert Text to Audio](https://github.com/GuillaumeFalourd/formulas-python/tree/master/convert/text-to-audio): `rit convert text-to-audio`
- [Face Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/face/recognition): `rit face recognition`
- [Speech Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/speech/recognition): `rit speech recognition`
- [Text Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/text/recognition): `rit text recognition`
  - [Image Text Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/detect/text-on-image): `rit detect image-to-text`
  - [Live Text Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/detect/text-on-video): `rit detect text-on-video`
- [Wikipedia Search](https://github.com/GuillaumeFalourd/formulas-python/tree/master/wiki/search): `rit wiki search`
- [Send Email](https://github.com/GuillaumeFalourd/formulas-python/tree/master/send/email): `rit send email`
- [Snake Game](https://github.com/GuillaumeFalourd/formulas-python/tree/master/game/snake): `rit game snake`
- [Flappy Bird Game](https://github.com/GuillaumeFalourd/formulas-python/tree/master/game/flappy-bird): `rit game flappy-bird`
- [Space Invasion Game](https://github.com/GuillaumeFalourd/formulas-python/tree/master/game/space-invasion): `rit game space-invasion`
- [Pacman Game](https://github.com/GuillaumeFalourd/formulas-python/tree/master/game/pacman): `rit game pacman`

### Working On

- [Aws boto3](https://github.com/GuillaumeFalourd/formulas-python/tree/master/aws/boto3): `rit aws boto3`
- [Linkedin web-scraping](https://github.com/GuillaumeFalourd/formulas-python/tree/master/linkedin/web-scraping): `rit linkedin web-scraping`
- [Object Detection](https://github.com/GuillaumeFalourd/formulas-python/tree/master/object/detection): `rit object detection`

## Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/install-cli)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal (since CLI version 2.8.0):

```bash
rit add repo --provider="Github" --name="formulas-python" --repoUrl="https://github.com/GuillaumeFalourd/formulas-python" --priority=1
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.

## Contribute to the repository with your formulas

### Creating formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Check the step by step of [how to create formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-create-formulas)
4. Add your formulas to the repository
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

### Updating Formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Add the cloned repository to your workspaces (`rit add workspace`) with a highest priority (for example: 1).
4. Check the step by step of [how to implement formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-implement-a-formula)
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

➡️ [Contribute to Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md) 💡
