# Ritchie Formula

## Premisses

To execute this formula, you need an email address and password set on Ritchie credentials.
*They will be asked automatically on the first formula execution*

⚠️ Google is not allowing you to log in via **smtplib** because it has flagged this sort of login as "less secure".

To allow the formula to work, go to [this link](https://www.google.com/settings/security/lesssecureapps) while you're logged in to your google account (set in the credential), and enable the access.

![Google](/docs/img/less-secure-apps.png)

## Command

```bash
rit send email
```

```bash
rit send email --docker
```

## Description

A formula to send an email to a specific address using [email_to](https://pypi.org/project/email-to/) python library.

The user may inform 3 inputs:

- the receiver email address
- the email subject (title)
- the email message (body)

## Sample

![Formula](/docs/img/rit-send-email.png)

![Result](/docs/img/rit-send-email-message.png)
