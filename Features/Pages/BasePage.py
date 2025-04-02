class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def enter_into_element(self, locator_type, locator_value, text_to_be_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.send_keys(text_to_be_entered)

    def get_element(self,locator_type,locator_value):
        element = None
        if locator_type.endswith('_xpath'):
            element = self.driver.find_element('xpath', locator_value)
        elif locator_type.endswith('_id'):
            element = self.driver.find_element('id', locator_value)
        else:
            element = self.driver.find_element('css selector', locator_value)
        return element

