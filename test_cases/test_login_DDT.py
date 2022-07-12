import time

from selenium import webdriver

from pageobjects.login_page import LoginPage
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from utilities import XLUtilties

class TestLogin_DDT_002:

    url = Readconfig.getApplicationURL()
    path = ".//Testdata/loginfile.xlsx"
    logger = LogGen.logging()

    def test_login_DDT(self, setup):
        self.logger.info("********** Test login DDT*************")
        self.logger.info("********Verify the Login DDT test******")
        self.driver = setup
        self.driver.get(self.url)

        self.lp = LoginPage(self.driver)
        self.row = XLUtilties.getRowcount(self.path, "Sheet1")
        print("No of rows in excel:", self.row)

        lst_status = []

        for r in range(2,self.row+1):
            self.user = XLUtilties.readdata(self.path, "Sheet1", r, 1)
            self.password = XLUtilties.readdata(self.path, "Sheet1", r, 2)
            self.exp = XLUtilties.readdata(self.path, "Sheet1", r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.set_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("*****Passed*****")
                    self.lp.logout_button()
                    lst_status.append("pass")
                elif self.exp == 'fail':
                    self.logger.info("****Fail*****")
                    self.lp.logout_button()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("****Failed*****")
                    lst_status.append("fail")
                elif self.exp == 'fail':
                    self.logger.info("******Passed*******")
                    lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("*********Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Failed DDT Login test**********")
            self.driver.close()
            assert False

        self.logger.info("*************End of the login test**********")
        self.logger.info("***********Completed TestLogin_DDT_002************")




