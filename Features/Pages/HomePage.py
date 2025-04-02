class HomePage:

    def __init__(self, driver):
        self.driver = driver

    leave_text_xpath = '//input[@class="oxd-input oxd-input--active"]'
    menus = '//ul[@class="oxd-main-menu"]/li/a/span'

    def enter_leave_text(self, text):
        self.driver.find_element('xpath', self.leave_text_xpath).send_keys(text)

    # def list_of_menu(self):
    #     self.driver.find_elements('xpath', self.menus)
