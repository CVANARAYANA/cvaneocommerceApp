from selenium import webdriver

from pageobjects.login_page import LoginPage
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen

class TestLogin:

    url = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    logger = LogGen.logging()

    def test_loginpage_title(self, setup):
        self.logger.info("************* Login page title Test 001 **********")
        self.logger.info("*************** Varify Home page title *************")
        self.driver = setup
        self.driver.get(self.url)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Test passed **********")

        else:
            self.driver.close()
            self.logger.error("********* Test failed *************")
            assert False


    def test_login_page(self, setup):
        self.logger.info("********** Test login page*************")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.set_login()
        login_title = self.driver.title
        if login_title == "Dashboard / nopCommerce administration":
            self.logger.info("************ Test passed ************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("\\Screenshots\\"+"test_login_page.png")
            self.driver.close()
            self.logger.error("********* Test failed *************")
            self.driver.close()
            assert False
