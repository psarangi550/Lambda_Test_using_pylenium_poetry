import os
from selenium import webdriver
import pytest
import urllib3
from selenium.webdriver.edge.service import Service

@pytest.fixture
def selenium_driver():
    username =os.getenv("LT_USERNAME")
    access_key=os.getenv("LT_ACCESS_KEY")
    remote_url=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    capabilities = {
		'LT:Options' : {
			"user" : "psarangi50",
			"accessKey" : "f0kClPeDcZ8sp9CrpmHxFsKYz7NTEhQ2m5n83MQuCeElH213I0",
			"build" : "your build name",
			"name" : "your test name",
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
# @pytest.fixture(scope="function")
# def selenium_driver():
#     service=Service()
#     driver=webdriver.Edge(service=service)
#     yield driver
#     driver.close()
#     driver.quit()

