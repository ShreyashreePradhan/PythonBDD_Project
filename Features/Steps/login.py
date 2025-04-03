import time

from behave import *

from Features.Pages.LoginPage import LoginPage


@given(u'I got navigated to OrangeHRM')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.assert_login_text() == 'Login'

    # assert context.driver.find_element('xpath', '//h5[text()="Login"]').text == 'Login'


@when(u'I enter username as "{username}"')
def step_impl(context,username):
    context.login_page.enter_username(username)

    # context.driver.find_element('xpath', '//input[@name="username"]').send_keys('Admin')


@when(u'I enter password as "{password}"')
def step_impl(context,password):
    context.login_page.enter_password(password)

    # context.driver.find_element('xpath', '//input[@type="password"]').send_keys('admin123')


@when(u'I click on login')
def step_impl(context):
    context.login_page.click_on_login()

    # context.driver.find_element('xpath', '//button[@type="submit"]').click()


@then(u'I should see "{homepage_text}" in homepage')
def step_impl(context, homepage_text):
    assert context.login_page.assert_dashboard_text() == homepage_text, 'user logged in'

    # assert context.driver.find_element('xpath', '//h6[text()="Dashboard"]').text == 'Dashboard', 'user logged in'


@when(u'I enter invalid username as "{username}"')
def step_impl(context,username):
    context.login_page.enter_username(username)

    # context.driver.find_element('xpath', '//input[@name="username"]').send_keys('adm')


@when(u'I enter invalid password as "{password}"')
def step_impl(context,password):
    context.login_page.enter_password(password)
    # context.driver.find_element('xpath', '//input[@type="password"]').send_keys('23')


@then(u'I should see "{invalid_text}" in loginpage')
def step_impl(context, invalid_text):
    assert context.login_page.invalid_credentials() == invalid_text

    # assert context.driver.find_element('xpath', '//p[text()="Invalid credentials"]').text == 'Invalid credentials'
