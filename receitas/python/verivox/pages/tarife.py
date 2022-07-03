from selenium.common.exceptions import NoSuchElementException
from pages.base import Base
from .locators.general_locators import GeneralLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class Tarife(Base):
    def how_many_tariffs(self):
        elements = WebDriverWait(self.drive, 30).until(EC.presence_of_all_elements_located((
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Tarife\")')))
        for i in range(len(elements)):
            try:
                value = int((elements[i].text).split()[0])
                if type(value) == int:
                    return value
            except:
                pass


    def check_if_are_all_tariffs_100_mbits(self):
        pass

    def scroll_to_the_end_of_page(self):
        pass