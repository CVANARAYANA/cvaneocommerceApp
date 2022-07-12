from selenium.webdriver.common.by import By


class LoginPage:

    login_username = "Email"
    login_password = "Password"
    login_button = "//button[@type='submit']"
    logout_button = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.login_username).clear()
        self.driver.find_element(By.ID, self.login_username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.login_password).clear()
        self.driver.find_element(By.ID, self.login_password).send_keys(password)

    def set_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def set_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button).click()

