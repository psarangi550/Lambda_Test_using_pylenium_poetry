from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Tests.Lamda_Todolist_Test.utility.test_base_class import TestBaseClass


class TestTodo:

    def __init__(self,setup02)->None:
        self.driver=setup02

    def goto(self)->'TestTodo':
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        return self
    
    def get_element(self, name):
        return self.driver.find_element(By.XPATH ,f"//span[text()='{name}']/parent::li/input[1]")

    def get_all_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")    


@pytest.fixture(scope="function")
def page(setup02)->TestTodo:
    return TestTodo(setup02).goto()

def test_click(page)->None:
    page.goto()
    page.get_element("First Item").click()
    assert page.get_element("First Item").is_selected()



 
