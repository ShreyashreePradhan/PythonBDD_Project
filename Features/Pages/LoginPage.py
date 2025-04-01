class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    login_button_xpath = '//button[@type="submit"]'
    username_xpath = '//input[@name="username"]'
    password_xpath = '//input[@type="password"]'

    def click_on_login(self):
        self.driver.find_element('xpath', self.login_button_xpath).click()

    def enter_username(self, username_text):
        self.driver.find_element('xpath', self.username_xpath).send_keys(username_text)

    def enter_password(self, password_text):
        self.driver.find_element('xpath', self.password_xpath).send_keys(password_text)



