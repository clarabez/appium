from time import sleep
from .base import Page
from .locators.login_locators import *


class Login:
    def __init__(self, driver):
        Page.__init__(self, driver)

    def goto_login_page(self, url):
        self.open(url)

    def insert_username(self, username):
        insert_username = self.find_element(LoginPageLocators.USERNAME)
        insert_username.send_keys(username)

    def insert_password(self, password):
        insert_password = self.find_element(LoginPageLocators.PASSWORD)
        insert_password.send_keys(password)

    def click_cancel(self):
        pass

    def click_login(self):
        btn_login = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        btn_login.click()

    def enter_login_credentials(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        sleep(2)
        self.click_login()
