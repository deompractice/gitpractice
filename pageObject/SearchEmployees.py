

import pytest
import time

from selenium.common.exceptions import NoSuchElementException as Ec
from selenium import webdriver
from selenium.webdriver.common.by import By



class search_employees:

    Click_CustomerOption_XPATH = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    Click_Customers_XPATH = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Text_Email_XPATH = (By.XPATH, "//input[@id='SearchEmail']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@id='SearchFirstName']")
    Text_LastName_XPATH = (By.XPATH, "//input[@id='SearchLastName']")
    Text_DateOfBrith_Month_XPATH = (By.XPATH, "//select[@id='SearchMonthOfBirth']")
    Text_DateOfBrith_Day_XPATH = (By.XPATH, "//select[@id='SearchDayOfBirth']")
    Text_RegistrationDate_From_XPATH = (By.XPATH, "//input[@id='SearchRegistrationDateFrom']")
    Text_RegistrationDate_To_XPATH = (By.XPATH, "//input[@id='SearchRegistrationDateTo']")
    Text_LastActivity_From_XPATH = (By.XPATH, "//input[@id='SearchLastActivityFrom']")
    Text_LastActivity_To_XPATH = (By.XPATH, "//input[@id='SearchLastActivityTo']")
    Text_Company_XPATH = (By.XPATH, "//input[@id='SearchCompany']")
    Text_IpAddress_XPATH = (By.XPATH, "//input[@id='SearchIpAddress']")
    Text_CustomerRole_XPATH = (By.XPATH, "//input[@role='listbox']")
    Click_Search_XPATH = (By.XPATH, "//button[@id='search-customers']")
    Search_Status_XPATH = (By.XPATH, "//td[normalize-space()='Registered']")



    def __init__(self, driver):
        self.driver = driver


    def Click_CustomerOption(self):
        self.driver.find_element(*search_employees.Click_CustomerOption_XPATH).click()


    def Click_Customers(self):
        self.driver.find_element(*search_employees.Click_Customers_XPATH).click()


    def Enter_Email(self,email):
        self.driver.find_element(*search_employees.Text_Email_XPATH).send_keys(email)


    def Enter_FirstName(self, firstname):
        self.driver.find_element(*search_employees.Text_FirstName_XPATH).send_keys(firstname)


    def Enter_LastName(self, lastname):
        self.driver.find_element(*search_employees.Text_LastName_XPATH).send_keys(lastname)


    def Click_Search(self):
        self.driver.find_element(*search_employees.Click_Search_XPATH).click()


    def Search_Status(self):

        try:
            self.driver.find_element(*search_employees.Search_Status_XPATH)
            return True

        except Ec:
            return False




