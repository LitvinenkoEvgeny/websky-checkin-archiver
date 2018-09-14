# -*- coding: utf-8 -*-

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class Archiver(object):
    def __init__(self, **kwargs):
        super(Archiver, self).__init__()

        self.WEBSKY_SITES = [
             'https://booking.nordstar.ru/websky/#/search',
             'https://booking.flyone.md/websky/#/search',
             'https://booking.georgian-airways.com/websky/search#/search',
             'https://booking.flyredwings.com/websky/#/search',
             'https://booking.angara.aero/websky/#/search',
             'https://booking.bekair.aero/websky/#/search',
             'http://booking.polarair.ru/websky/#/search',
             'https://airbook.nordwindairlines.ru/online/#/search',
             'http://booking.flyaurora.ru/websky/#/search',
             'http://booking.tajikairlines.com/websky/#/search',
             'https://booking.scat.kz/websky/#/search',
             'https://booking.azurair.ru/websky/#/search',
             'https://booking.iraero.ru/websky/#/search',
             'https://book.yamal.aero/websky/search#/search',
             'https://www.nordavia.ru/book/?lang=ru#/search',
             'https://booking.somonair.com/websky/#/search',
             'https://booking.izhavia.su/websky/#/search',
             'https://booking.alrosa.aero/websky/#/search',
             'https://web-checkin.severstal-avia.ru/websky/search#/search'
        ]

        self.CHECKIN_SITES = [
            'https://airbook.nordwindairlines.ru/check-in/',
            'https://www.nordavia.ru/check/',
            'https://booking.nordstar.ru/check-in/',
            'https://booking.flyone.md/websky-check-in/',
            'https://booking.flyredwings.com/websky-check-in/',
            'https://booking.bekair.aero/webcheck-in/',
            'https://ticket.rusline.aero/websky-check-in/'
        ]

        self.login = kwargs['login']
        self.password = kwargs['password']
        self.driver_options = webdriver.ChromeOptions()


        # set download default directory
        # options.add_experimental_option('prefs', {"download.default_directory": os.path.realpath(os.path.join(os.getcwd(), 'arch', 'nordwind'))})
        # self.driver = webdriver.Chrome(chrome_options=self.driver_options)


        # chrome = webdriver.Chrome(chrome_options=options)
        # chrome.get(WEBSKY_SITES[0])
        # WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "orderSearchForm")))
        # go_to_admin(chrome, LOGIN, PASSWORD)
        # download_params(chrome)
        # download_aliases(chrome)

    def start_download(self):
        Archiver.set_drivers_dir_to_path()

        for websky_site in self.WEBSKY_SITES:
            websky_site_name = Archiver.get_aviacompany_name(websky_site)
            self.driver_options.add_experimental_option('prefs', {
                "download.default_directory": os.path.realpath(os.path.join(os.getcwd(), 'arch', websky_site_name, 'websky'))
            })
            self.driver = webdriver.Chrome(chrome_options=self.driver_options)
            self.driver.get(websky_site)
            self.wait_for_class('orderSearchForm')
            self.go_to_admin()

    def wait_for_class(self, class_name):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    def go_to_admin(self):
        admin_url = Archiver.create_admin_url(self.driver.current_url)
        self.driver.get(admin_url)
        login_form = self.wait_for_class('login-form')
        login_input = self.driver.find_element_by_xpath('//input[@name="login"]')
        password_input = self.driver.find_element_by_xpath('//input[@name="password"]')
        login_input.send_keys(self.login)
        password_input.send_keys(self.password)
        submit_button = self.driver.find_element_by_xpath('//button[@class="ng-binding"]').click()
        time.sleep(1)
        
    @staticmethod
    def get_aviacompany_name(url):
        return url.split('.')[1]
    
    @staticmethod
    def set_drivers_dir_to_path():
        os.environ["PATH"] += ':' + os.path.realpath(os.path.join(os.getcwd(), 'drivers'));

    @staticmethod
    def create_admin_url(now_url):
        return re.sub(r'\/(\?.+|#.+|search)', '/admin', now_url)
        


# LOGIN = raw_input('Логин: ')
# PASSWORD = raw_input('Пароль: ')
archiver.start_download()




