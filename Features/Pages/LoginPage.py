from Features.Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    login_xpath = '//h5[text()="Login"]'
    login_button_xpath = '//button[@type="submit"]'
    username_xpath = '//input[@name="username"]'
    password_xpath = '//input[@type="password"]'
    dashboard_xpath = '//h6[text()="Dashboard"]'
    invalid_credentials_xpath = '//p[text()="Invalid credentials"]'

    def assert_login_text(self):
        return self.get_element('login_xpath', self.login_xpath).text

        # return self.driver.find_element('xpath', self.login_xpath).text

    def click_on_login(self):
        self.click_on_element('login_button_xpath', self.login_button_xpath)

        # self.driver.find_element('xpath', self.login_button_xpath).click()

    def enter_username(self, username_text):
        self.enter_into_element('username_xpath', self.username_xpath, username_text)

        # self.driver.find_element('xpath', self.username_xpath).send_keys(username_text)

    def enter_password(self, password_text):
        self.enter_into_element('password_xpath', self.password_xpath, password_text)

        # self.driver.find_element('xpath', self.password_xpath).send_keys(password_text)

    def assert_dashboard_text(self):
        return self.get_element('dashboard_xpath', self.dashboard_xpath).text

        # return self.driver.find_element('xpath', self.dashboard_xpath).text

    def invalid_credentials(self):
        return self.get_element('nvalid_credentials_xpath', self.invalid_credentials_xpath).text

        # return self.driver.find_element('xpath', self.invalid_credentials_xpath).text
