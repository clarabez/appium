from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
from pages.base import Base
from .locators.general_locators import *
import time


class Vergleich(Base):
    def reach_(self):
        btn_dsl = Base.find_element(self.drive, GeneralLocators.button_dsl)
        btn_dsl.click()
        area_code_field = Base.find_element(self.drive, GeneralLocators.area_code_field)
        area_code_field.click()
        area_code_field.send_keys('030')
        time.sleep(30)
        # Base.handle_cookie(self.drive)
        cookie = Base.find_element(self.drive, GeneralLocators.button_cookie)
        cookie.click()
        time.sleep(10)
        mbit_value = Base.find_element(self.drive, GeneralLocators.mbit_100)
        mbit_value.click()
        button_vergleichen = Base.find_element(self.drive, GeneralLocators.button_vergleichen)
        button_vergleichen.click()
