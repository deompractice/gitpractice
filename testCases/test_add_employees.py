

import time
from pageObject.LoginPage import loginpage
from pageObject.SearchEmployees import search_employees
from pageObject.AddEmployees import add_employees
from selenium.common.exceptions import NoSuchElementException as Ec


class Test_Add_Employees:

    def test_add_employees004(self,setup):
        self.driver = setup

        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login_Button()
        time.sleep(2)

        self.se1 = search_employees(self.driver)
        self.se1.Click_CustomerOption()
        self.se1.Click_Customers()

        self.ae = add_employees(self.driver)
        self.ae.Click_AddNew()
        self.ae.Enter_Email("automation123@gmail.com")
        self.ae.Enter_Frist_Name("A")
        self.ae.Enter_Last_Name("B")
        self.ae.Click_Gender()
        self.ae.Enter_Company_Name("ABC")
        self.ae.Click_Save_And_Continue()

        try:
            self.ae.Display_Add_Status()
            print("Test is Pass")
            self.lp.Click_Logout_Button()
            return True

        except Ec:
            return False



