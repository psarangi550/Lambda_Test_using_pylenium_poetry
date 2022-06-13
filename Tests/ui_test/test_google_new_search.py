from asyncio.log import logger
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def test_search(setUp01,get_logger):
    setUp01.get('https://www.google.com/')
    ac=ActionChains(setUp01)
    searchbox=setUp01.find_element(By.NAME,"q")
    ac.click(searchbox).perform()
    searchbox.send_keys("puppies",Keys.ENTER)
    time.sleep(10)
    get_logger.info(setUp01.title)
    assert setUp01.title == "puppies - Google Search"