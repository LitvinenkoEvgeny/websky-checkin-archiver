# -*- coding: utf-8 -*-

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base import BaseSelenium

class Screenshooter(BaseSelenium):
    def __init__(self, driver, sitename, directory):
        super(Screenshooter, self).__init__(driver, sitename, directory)
        self.driver = driver
        self.sitename = sitename
        self.directory = directory
        self.screenshot_directory = os.path.join(self.directory, 'screenshots')

        if not os.path.exists(self.screenshot_directory):
            os.makedirs(self.screenshot_directory)

    def start(self):
        print(self.wait_for_class('orderSearchForm'))
        self.url = self.driver.current_url
        self.do_main_page_screenshot()

    def do_main_page_screenshot(self):
        self.maximize_window()
        self.take_screenshot('main_page')
        time.sleep(20)


    def take_screenshot(self, name):
        self.driver.save_screenshot(self.screenshot_directory + os.path.sep + name + '.png')

    def take_screenshots_in_all_sizes(self, name):
        driver.maximize_window()
        self.take_screenshot(name + '_desktop')
        mobile_emulation = { "deviceName": "Nexus 5" }
