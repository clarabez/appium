from pages.base import Base
from .locators.login_locators import *


class Home(Base):
    def goto_login_page(self):
        """
        This method performs the path to reach Login activity
        :return: None
        """
        btn_menu = Base.find_element(self.drive, LoginPageLocators.HAMBURGUER_MENU)
        btn_menu.click()
        btn_sign = Base.find_element(self.drive, LoginPageLocators.LOGIN)
        btn_sign.click()
