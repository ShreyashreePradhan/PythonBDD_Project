class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    login_button_xpath = '//button[@type="submit"]'

    def click_on(self):
        self.driver.find_element('xpath', self.login_button_xpath).click()


