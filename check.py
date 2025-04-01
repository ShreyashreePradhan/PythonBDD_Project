import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/shreya/Downloads/geckodriver"
service = Service(chrome_driver_path)
# opts = webdriver.ChromeOptions()

# opts.add_experimental_option("detach", True)
driver = webdriver.Firefox(service=service)
time.sleep(5)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
