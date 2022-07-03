from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators.general_locators import *
import time


class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def find_element(self, element):
        wait = WebDriverWait(self, 240)
        value = wait.until(EC.presence_of_element_located((
            element
        )))
        return value

    def handle_cookie(self):
        self.drive.switch_to.context()
        element = self.find_element(GeneralLocators.button_cookie)
        if element.is_displayed():
            element.click()
            time.sleep(6)



