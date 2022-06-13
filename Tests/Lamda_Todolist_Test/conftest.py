from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import urllib3
import os
from dotenv import load_dotenv
load_dotenv() #calling the load_dotenv to load the .env file variable

@pytest.fixture(scope="function")
def setup02():
    username =os.getenv("LT_USERNAME")
    access_key=os.getenv("LT_ACCESS_KEY")
    remote_url=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    capabilities = {
		'LT:Options' : {
			"user" : "psarangi50",
			"accessKey" : "f0kClPeDcZ8sp9CrpmHxFsKYz7NTEhQ2m5n83MQuCeElH213I0",
			"build" : "Todo Build",
			"name" : "Todo Build run",
			"platformName" : "Windows 11"
		},
		"browserName" : "MicrosoftEdge",
		"browserVersion" : "102.0",
	}
    driver=webdriver.Remote(command_executor=remote_url,desired_capabilities=capabilities)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    yield driver
    driver.close()
    driver.quit()