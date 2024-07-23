from selenium.webdriver.common.by import By
# page_url = https://www38.polyu.edu.hk/eStudent/login.jsf
class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www38.polyu.edu.hk/eStudent/login.jsf"

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        user_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[maxlength='9']")
        user_name_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='j_password']")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()
