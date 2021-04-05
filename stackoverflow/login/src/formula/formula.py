#!/usr/bin/python3
import os

import sendgrid
from sendgrid.helpers.mail import Mail

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def run(email, password, display_name):
    print("🤖 Logging into stackoverflow.com")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        driver.get("https://stackoverflow.com")

        driver.find_element_by_link_text("Log in").click()

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit-button").submit()

        driver.find_element_by_class_name("my-profile").click()

        elem = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "grid--cell.ws-nowrap.fs-body3"))
        )
        assert display_name in elem.text
        print("\n✅ Logged into stackoverflow.com and accessed profile page.")

    except Exception as e:
        message = "❌ An error occurred while trying to access stackoverflow.com!"
        print(message)
        send_mail("Error at login!", message + str(e))

    finally:
        driver.close()

def send_mail(subject, content):
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('RIT_SENDGRID_API_KEY'))

        from_email = os.environ.get('RIT_SENDGRID_EMAIL_SENDER')
        to_email = os.environ.get('RIT_STACKOVERFLOW_EMAIL'),

        message = Mail(
            from_email = from_email,
            to_emails = to_email,
            subject = subject,
            html_content = content
        )

        response = sg.client.mail.send.post(request_body=message.get())

        print(f"📩 Email sent successfully to {to_email}")
    
    except Exception as e:
        print("❌ An error occurred while trying to send the email!")
