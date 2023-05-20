import pytest
from selenium import webdriver
import time
from pageObject.LoginPage import loginpage
from selenium.common.exceptions import NoSuchElementException as Ec

class Test_Page_Title:

    def test_page_title002(self,setup):
        self.driver = setup

        self.lp = loginpage(self.driver)

        self.lp.Enter_UserName("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login_Button()
        time.sleep(2)

        try:
            self.lp.Login_Status()
            print("test case is passed")
            self.driver.save_screenshot("D:\\Python Selenium Automation Notes\\NonCommerces\\ScreenShot\\NonCommerces.png")
            self.lp.Click_Logout_Button()
            return True

        except Ec:
            return False
















