

import pytest
import time

from selenium.common.exceptions import NoSuchElementException as Ec
from selenium import webdriver
from selenium.webdriver.common.by import By



class add_employees:

    Click_Add_New_XPATH = (By.XPATH, "//a[@class='btn btn-primary']")
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@id='FirstName']")
    Text_LastName_XPATH = (By.XPATH, "//input[@id='LastName']")
    Click_Gender_XPATH= (By.XPATH, "//label[@for='Gender_Male']")
    Text_CompanyName_XPATH = (By.XPATH, "//input[@id='Company']")
    Click_SaveAndContinue_XPATH = (By.XPATH, "//button[@name='save-continue']")
    Add_Status_XPATH = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")


    def __init__(self,driver):
        self.driver = driver

    def Click_AddNew(self):
        self.driver.find_element(*add_employees.Click_Add_New_XPATH).click()


    def Enter_Email(self, email):
        self.driver.find_element(*add_employees.Text_Email_XPATH).send_keys(email)


    def Enter_Frist_Name(self, firstname):
        self.driver.find_element(*add_employees.Text_FirstName_XPATH).send_keys(firstname)


    def Enter_Last_Name(self, lastname):
        self.driver.find_element(*add_employees.Text_LastName_XPATH).send_keys(lastname)


    def Click_Gender(self):
        self.driver.find_element(*add_employees.Click_Gender_XPATH).click()


    def Enter_Company_Name(self, companyname):
        self.driver.find_element(*add_employees.Text_CompanyName_XPATH).send_keys(companyname)


    def Click_Save_And_Continue(self):
        self.driver.find_element(*add_employees.Click_SaveAndContinue_XPATH).click()


    def Display_Add_Status(self):

        try:
            self.driver.find_element(*add_employees.Add_Status_XPATH)
            return True

        except Ec:
            return False


















