from selenium.common.exceptions import NoSuchElementException

from pages.base import Base
from .locators.login_locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(Base):
    def get_error_message(self):
        """
        This method collects and returns error message on login page
        :return: displayed message
        """
        wait = WebDriverWait(self.drive, 10)
        value = wait.until(EC.presence_of_element_located((
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
                            'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'LinearLayout[1]/android.widget.TextView[2]'
        )))
        return value.text

    def insert_username(self, username):
        """
        This method inserts username value on username field for Login
        :param username: username value
        :return: None
        """
        wait = WebDriverWait(self.drive, 10)
        name = wait.until(EC.presence_of_element_located((
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
                            'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'LinearLayout[1]/TextInputLayout[1]/android.widget.EditText'
        )))
        name.send_keys(username)

    def insert_password(self, password):
        """
        This method inserts password value on password field for Login
        :param password:
        :return: None
        """
        wait = WebDriverWait(self.drive, 10)
        name = wait.until(EC.presence_of_element_located ((
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
                            'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'LinearLayout[1]/TextInputLayout[2]/android.widget.EditText'
        )))
        name.send_keys(password)

    def click_login(self):
        """
        This method performs a click on Login button, on Login screen
        :return: None
        """
        wait = WebDriverWait(self.drive, 10)
        value = wait.until(EC.presence_of_element_located((
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
                            'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'LinearLayout[2]/android.widget.TextView[2]'
        )))
        value.click()

    def click_cancel(self):
        """
        This method performs a click on Cancel button, on Login screen
        :return: None
        """
        wait = WebDriverWait(self.drive, 10)
        value = wait.until(EC.presence_of_element_located((
            MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
                            'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                            'LinearLayout[2]/android.widget.TextView[1]'
        )))
        value.click()

    def is_in_login_screen(self):
        """
        This method checks if current activity is Login one
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 10)
            wait.until(EC.presence_of_element_located((
                MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.'
                                'v4.widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.'
                                'RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.'
                                'LinearLayout/android.widget.Button'
            )))
        except NoSuchElementException:
            return False
        return True

    def is_logged(self):
        """
        This method checks if current activity is Logged one
        :return: boolean
        """
        try:
            wait = WebDriverWait(self.drive, 10)
            wait.until(EC.presence_of_element_located((
                MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.'
                                'v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.'
                                'ViewGroup/android.widget.TextView'
            )))
        except NoSuchElementException:
            return False
        return True
