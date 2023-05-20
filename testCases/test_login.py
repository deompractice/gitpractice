
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.LoginPage import loginpage



class Test_Login:

    def test_login001(self,setup):
        self.driver = setup

        self.lp = loginpage(self.driver)

        self.lp.Enter_UserName("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login_Button()
        time.sleep(2)

        self.lp.Click_Logout_Button()
        self.driver.close()













