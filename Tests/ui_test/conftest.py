import inspect
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
LOG_DIR=BASE_DIR.joinpath("Logs")
LOG_FILE=LOG_DIR.joinpath("test_google.log")


@pytest.fixture(scope="function")
def setUp01():
    service = Service(ChromeDriverManager().install())
    options =Options()
    options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver=webdriver.Chrome(service=service, options=options)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope="function")
def get_logger():
    logger = logging.getLogger(name=inspect.stack()[1][3])
    logger.setLevel(logging.INFO)
    filehandler=logging.FileHandler(LOG_FILE,mode="a")
    filehandler.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger

