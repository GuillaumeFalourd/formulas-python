#!/usr/bin/python3
from selenium import webdriver
import time
import re

def run(email, password, names, path):
    #Open Chrome web
    driver = webdriver.Chrome(executable_path='{}/chromedriver'.format(path))
    driver.get('https://www.linkedin.com/')

    #Login username/password
    email_box = driver.find_element_by_id('session_key')
    email_box.send_keys(email)
    pass_box = driver.find_element_by_id('session_password')
    pass_box.send_keys(password)
    submit_button = driver.find_element_by_class_name('sign-in-form__submit-button')
    submit_button.click()

    time.sleep(1)
    
    #For each name, retrive name, job, location, company and number of connections
    for name in names:
        try:
            driver.get('https://www.linkedin.com/search/results/index/?keywords=' + name)
            
            xpath = "(//span[text()='" + name + "'])[1]"
            time.sleep(5)
            driver.find_element_by_xpath(xpath).click()
            data = ''
            try :
                name = getName(driver)
                data += name + ','
            except Exception as ex:
                data += '0,'
                
            try :
                job = getJob(driver)
                data += job + ','
            except Exception as ex:
                data += '0,'
        
            try:
                loc = getLocation(driver)
                data += loc + ','
            except Exception as ex:
                data += '0,'

            try:
                comp = getCompany(driver)
                data += comp + ','
            except Exception as ex:
                data += '0,'
                
            try:
                edu = getEducation(driver)
                data += edu + ','
            except Exception as ex:
                data += '0,'

            try:
                conn = getConnections(driver)
                data += conn + ','
            except Exception as ex:
                data += '0,'	
                
            #print (data)
            saveAsCSV(data)
            print("✅ linkedin_result.csv file created successfully")
        except Exception as e:
            print("Exception in retrieving data" + e)

def getName(driver):
    xpath = "//li[contains(@class, 'inline t-24 t-black t-normal break-words')]"
    time.sleep(5)
    name = driver.find_element_by_xpath(xpath).text
    return name

def getJob(driver):
	xpath = "//h2[contains(@class, 'mt1 t-18 t-black t-normal break-words')]"
	job = driver.find_element_by_xpath(xpath).text
	return job

def getLocation(driver):
    xpath = "//li[contains(@class, 't-16 t-black t-normal inline-block')]"
    loc = driver.find_element_by_xpath(xpath).text
    re_loc = re.sub(",", " -", loc)
    return re_loc

def getCompany(driver):
	xpath = "//a[contains(@data-control-name, 'position_see_more')]"
	comp = driver.find_element_by_xpath(xpath).text
	return comp

def getEducation(driver):
	xpath = "//a[contains(@data-control-name, 'education_see_more')]"
	edu = driver.find_element_by_xpath(xpath).text
	return edu

def getConnections(driver):
	xpath = "//a[contains(@data-control-name, 'topcard_view_all_connections')]"
	conn = driver.find_element_by_xpath(xpath).text
	return conn

def saveAsCSV(data):
    fileName = "linkedin_result.csv"
    f = open(fileName, "a")
    headers="Name,Job,Location,Company,Education,Connections\n"
    f.write(data + '\n')
