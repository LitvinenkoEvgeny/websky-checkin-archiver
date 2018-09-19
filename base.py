# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseSelenium(object):
    '''

    Лень выносить все что нужно в суперкласс, 
    пускай будет только необходимый минимум

    '''
    def __init__(self, *args, **kwargs):
        super(BaseSelenium, self).__init__()
    
    def wait_for_class(self, class_name):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    def wait_for_xpath(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def maximize_window(self):
        self.driver.maximize_window()

        