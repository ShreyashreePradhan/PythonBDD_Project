import time

from behave import *

from Features.Pages.HomePage import HomePage
from Features.Pages.LoginPage import LoginPage


@given(u'I logged in to OrangeHRM')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_username('Admin')
    context.login_page.enter_password('admin123')
    context.login_page.click_on_login()

    # context.driver.find_element('xpath', '//input[@name="username"]').send_keys('Admin')
    # context.driver.find_element('xpath', '//input[@type="password"]').send_keys('admin123')
    # context.driver.find_element('xpath', '//button[@type="submit"]').click()


@when(u'I search "{module_name}"')
def step_impl(context, module_name):
    time.sleep(2)
    context.home_page = HomePage(context.driver)
    context.home_page.enter_leave_text(module_name)

    # context.driver.find_element('xpath', '//input[@class="oxd-input oxd-input--active"]').send_keys("Leave")


@then(u'I only see "{module_name}" module')
def step_impl(context, module_name):
    time.sleep(2)
    # context.list_of_menus = context.home_page.list_of_menu()
    context.list_of_menus = context.driver.find_elements('xpath', '//ul[@class="oxd-main-menu"]/li/a/span')
    assert len(context.list_of_menus) == 1
    for i in context.list_of_menus:
        assert i.text == module_name
        break
