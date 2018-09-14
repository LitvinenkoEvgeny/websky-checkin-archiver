import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class Archiver(object):
    def __init__(self, *args):
        super(Archiver, self).__init__(**kwargs)

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

    def start_download(self, site_config):
        pass
        

