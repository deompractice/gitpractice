
import pytest
import time

from selenium.common.exceptions import NoSuchElementException as Ec
from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage:
    Text_UserName_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    Login_Status_XPATH = (By.XPATH, "//div[@class='card-title'][normalize-space()='NopCommerce News']")
    Click_Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")



    def __init__(self,driver):
        self.driver = driver

    def Enter_UserName(self, username):
        self.driver.find_element(*loginpage.Text_UserName_XPATH).clear()
        self.driver.find_element(*loginpage.Text_UserName_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*loginpage.Text_Password_XPATH).clear()
        self.driver.find_element(*loginpage.Text_Password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        self.driver.find_element(*loginpage.Login_Status_XPATH)

    def Click_Logout_Button(self):
        self.driver.find_element(*loginpage.Click_Logout_Button_XPATH).click()

    def Login_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*loginpage.Login_Status_XPATH)
            return True

        except Ec:
            return False


