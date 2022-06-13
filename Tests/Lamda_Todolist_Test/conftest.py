from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from Tests.Lamda_Todolist_Test.test_alterpage import TestTodo

@pytest.fixture(scope="function")
def setup02():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.binary_location="C:\\Users\\611903295\\Downloads\\Unhashed_Pylenium_Demo\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
    driver=webdriver.Chrome(service=service, options=options)
    yield driver
    driver.close()
    driver.quit()


