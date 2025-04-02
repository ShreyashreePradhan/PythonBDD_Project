import time

from behave import *

from Features.Pages.LoginPage import LoginPage


@given(u'I got navigated to OrangeHRM')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.assert_login_text() == 'Login'

    # assert context.driver.find_element('xpath', '//h5[text()="Login"]').text == 'Login'


@when(u'I enter username')
def step_impl(context):
    context.login_page.enter_username('Admin')

    # context.driver.find_element('xpath', '//input[@name="username"]').send_keys('Admin')


@when(u'I enter password')
def step_impl(context):
    context.login_page.enter_password('admin123')

    # context.driver.find_element('xpath', '//input[@type="password"]').send_keys('admin123')


@when(u'Click on login')
def step_impl(context):
    context.login_page.click_on_login()

    # context.driver.find_element('xpath', '//button[@type="submit"]').click()


@then(u'User should land onto Homepage')
def step_impl(context):
    assert context.login_page.assert_dashboard_text() == 'Dashboard', 'user logged in'

    # assert context.driver.find_element('xpath', '//h6[text()="Dashboard"]').text == 'Dashboard', 'user logged in'


@when(u'I enter \'adm\'')
def step_impl(context):
    context.login_page.enter_username('adm')

    # context.driver.find_element('xpath', '//input[@name="username"]').send_keys('adm')


@when(u'I enter \'12\'')
def step_impl(context):
    context.login_page.enter_password('23')
    # context.driver.find_element('xpath', '//input[@type="password"]').send_keys('23')


@then(u'User should see "Invalid credentials"')
def step_impl(context):
    assert context.login_page.invalid_credentials() == 'Invalid credentials'

    # assert context.driver.find_element('xpath', '//p[text()="Invalid credentials"]').text == 'Invalid credentials'
