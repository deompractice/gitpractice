

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    return driver



