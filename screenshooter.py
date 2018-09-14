
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
    def __init__(self, driver, url, directory_to_save):
        super(Screenshooter, self).__init__(*args, **kwargs)
        self.driver = driver
        self.url = url
        self.directory_to_save = directory_to_save

    def start(self):
        pass
