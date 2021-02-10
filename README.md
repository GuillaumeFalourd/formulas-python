# Ritchie Formulas Repository - Python

![Rit banner](/docs/img/ritchie-banner.png)

## Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)

## Formulas available on this repository

### Done / To improve

- [Convert Text to Audio](https://github.com/GuillaumeFalourd/formulas-python/tree/master/convert/text-to-audio): `rit convert text-to-audio`
- [Speech Recognition](https://github.com/GuillaumeFalourd/formulas-python/tree/master/speech/recognition): `rit speech recognition`

### Doing

- [Aws boto3](https://github.com/GuillaumeFalourd/formulas-python/tree/master/aws/boto3): `rit aws boto3`
- [Linkedin web-scraping](https://github.com/GuillaumeFalourd/formulas-python/tree/master/linkedin/web-scraping): `rit linkedin web-scraping`
- [Schedule formula](https://github.com/GuillaumeFalourd/formulas-python/tree/master/schedule/formula): `rit schedule formula`
- [Send Email](https://github.com/GuillaumeFalourd/formulas-python/tree/master/send/email): `rit send email`
- [Convert Image to Text](https://github.com/GuillaumeFalourd/formulas-python/tree/master/convert/image-to-text): `rit convert image-to-text`

## Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/install-cli)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal:

**With Ritchie CLI stdin <= 2.8.0**

```bash
echo '{"provider":"Github", "name":"formulas-python", "url":"https://github.com/GuillaumeFalourd/formulas-python", "priority":1}' | rit add repo --stdin
```

**With Ritchie CLI input flags => 2.9.0**

```bash
rit add repo --name="formulas-python" --priority=1 --provider="Github" --repoUrl="https://github.com/ZupIT/formulas-python"
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

- [Contribute to Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md)
