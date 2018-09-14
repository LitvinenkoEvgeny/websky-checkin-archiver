# -*- coding: utf-8 -*-

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["PATH"] += ':' + os.path.realpath(os.path.join(os.getcwd(), 'drivers'));

WEBSKY_SITES = [
    'https://airbook.nordwindairlines.ru/websky-test/'
]

LOGIN = raw_input('Логин: ')
PASSWORD = raw_input('Пароль: ')

# TODO: move to class based archive

def create_admin_url(now_url):
    return re.sub(r'(\?.+|#.+)', 'admin', now_url)

def download_aliases(driver):
    go_to_aliases_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'admin#aliases')]")))
    go_to_aliases_button.click()
    # TODO: fix it!
    time.sleep(1)
    download_aliases_buttons = driver.find_elements_by_xpath('//a[contains(@href, "generate-aliases")]')
    for download_aliases_button in download_aliases_buttons:
        driver.get(download_aliases_button.get_attribute('href'))
    time.sleep(5)
        

def download_params(driver):
    download_params_button_wrapper = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-save-parameters")))
    download_params_button = download_params_button_wrapper.find_element_by_xpath('./a')
    download_link = download_params_button.get_attribute('href')
    driver.get(download_link)


def go_to_admin(driver, login, password):
    admin_url = create_admin_url(driver.current_url)
    driver.get(admin_url)
    login_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "login-form")))
    login_input = driver.find_element_by_xpath('//input[@name="login"]')
    password_input = driver.find_element_by_xpath('//input[@name="password"]')
    login_input.send_keys(login)
    password_input.send_keys(password)
    submit_button = driver.find_element_by_xpath('//button[@class="ng-binding"]').click()

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {"download.default_directory": os.path.realpath(os.path.join(os.getcwd(), 'arch', 'nordwind'))})
    chrome = webdriver.Chrome(chrome_options=options)
    chrome.get(WEBSKY_SITES[0])
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "orderSearchForm")))
    go_to_admin(chrome, LOGIN, PASSWORD)
    download_params(chrome)
    download_aliases(chrome)
    


if __name__ == '__main__':
    main()