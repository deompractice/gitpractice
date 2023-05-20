

import time
from pageObject.LoginPage import loginpage
from pageObject.SearchEmployees import search_employees
from selenium.common.exceptions import NoSuchElementException as Ec


class Test_Search_Employees:

    def test_search_employees003(self,setup):
        self.driver = setup

        self.lp = loginpage(self.driver)

        self.lp.Enter_UserName("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login_Button()
        time.sleep(2)

        self.se1 = search_employees(self.driver)

        self.se1.Click_CustomerOption()
        self.se1.Click_Customers()
        self.se1.Enter_Email("steve_gates@nopCommerce.com")
        self.se1.Enter_FirstName("Steve")
        self.se1.Enter_LastName("Gates")
        self.se1.Click_Search()
        time.sleep(2)

        try:
            self.se1.Search_Status()
            print("test case is Passed")
            self.lp.Click_Logout_Button()
            return True

        except Ec:
            return False

