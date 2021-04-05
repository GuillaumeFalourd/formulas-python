# Ritchie Formula

## Premisses

- Python 3.6+ (along with pip) installed
- Google Chrome installed
- The selenium driver for Google Chrome browser. 
[You can download the latest from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). After you unzip it, for convenience, on unix, you should place the chromedriver file under `/usr/local/bin/`
- A SendGrid [API KEY](https://sendgrid.com/docs/ui/account-and-settings/api-keys/) and [EMAIL SENDER](https://sendgrid.com/docs/ui/sending-email/senders/). It's `FREE` until 100 emails sent / day.

## Command

```bash
rit stackoverflow login
```

## Description

This formula uses Selenium with a Chrome Driver to connect to your stackoverflow account, which can be useful to earn the [Fanatic Badge](https://stackoverflow.com/help/badges/83/fanatic).

```bash
Visit the site each day for 100 consecutive days. (Days are counted in UTC.).
```

If an error occured, the formula will send an EMAIL to the Stackoverflow user account using SendGrid.

## Demo

![Execution](/docs/img/rit-stackoverflow-login.png)
