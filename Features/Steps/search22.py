# import time
#
# from behave import *
#
#
# @given(u'I logged in to OrangeHRM')
# def step_impl(context):
#     context.login()
#
#
# @when(u'I search \'Leave\'')
# def step_impl(context):
#     context.driver.find_element('xpath', '//input[@class="oxd-input oxd-input--active"]').send_keys("Leave")
#
#
# @when(u'I search \'Leave\'')
# def step_impl(context):
#     list_of_menus = context.driver.find_elements('xpath', '//ul[@class="oxd-main-menu"]')
#     assert (list_of_menus.text == 'Leave' and len(list_of_menus) == 1)
