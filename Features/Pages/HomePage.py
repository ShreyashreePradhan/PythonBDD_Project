from Features.Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    leave_text_xpath = '//input[@class="oxd-input oxd-input--active"]'
    menus_xpath = '//ul[@class="oxd-main-menu"]/li/a/span'

    def enter_leave_text(self, module_text):
        self.enter_into_element('leave_text_xpath',self.leave_text_xpath, module_text)

        #self.driver.find_element('xpath', self.leave_text_xpath).send_keys(text)

    def list_of_menu(self):
        return self.get_list_of_datas('menus_xpath',self.menus_xpath)

       # return self.driver.find_elements('xpath', self.menus_xpath)
