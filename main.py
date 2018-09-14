import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ["PATH"] += ':' + os.path.realpath(os.path.join(os.getcwd(), 'drivers'));
print(os.environ["PATH"])

driver = webdriver.Chrome()
driver.get('http://google.com')