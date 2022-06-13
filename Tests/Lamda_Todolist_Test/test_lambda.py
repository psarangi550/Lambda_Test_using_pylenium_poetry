import pytest
import time
from Tests.Lamda_Todolist_Test.utility.test_base_class import TestBaseClass
from selenium.webdriver.common.by import By

class TestLambdaTodo(TestBaseClass):
    def test_lambda(self)->None:
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        self.driver.find_element(By.XPATH,"//span[text()='First Item']/parent::li/input[1]").click()
        time.sleep(10)
        assert self.driver.find_element(By.XPATH,"//input[@name='li1']").is_selected()
        self.get_logger().info("success")
