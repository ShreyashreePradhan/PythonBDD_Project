from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath('/Users/shreya/PycharmProjects/pythonBDD_project/Features/environment.py'))))
from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name == 'chrome':
        chrome_driver_path = "/Users/shreya/Downloads/chromedriver/chromedriver"
        service = Service(chrome_driver_path)
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(options=opts, service=service)
    else:
        firefox_driver_path = "/Users/shreya/Downloads/geckodriver"
        service = Service(firefox_driver_path)
        context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration('basic info', 'url'))
    context.driver.implicitly_wait(30)



def after_scenario(context, drive):
    context.driver.quit()
