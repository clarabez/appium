import pytest
from pages.home import Home
from pages.login import Login
from utils import constants


@pytest.mark.usefixtures("test_setup")
class TestYahnac(object):
    def test_invalid_credentials(self, test_setup):
        """
        This method tests if it is possible to login using invalid credentials
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.insert_username(constants.credentials['invalid_username'])
        login.insert_password(constants.credentials['invalid_password'])
        login.click_login()
        message = login.get_error_message()
        assert message == constants.credentials['error_message'], "Unexpected message for wrong credentials"

    def test_empty_password_field(self, test_setup):
        """
        This method tests if it is possible to login using password only
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.insert_username(constants.credentials['valid_username'])
        login.click_login()
        message = login.get_error_message()
        assert message == constants.credentials['error_message'], "Unexpected message for wrong credentials"

    def test_empty_username_field(self, test_setup):
        """
        This method tests if it is possible to login using username only
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.insert_password(constants.credentials['valid_password_for_valid_username'])
        login.click_login()
        message = login.get_error_message()
        assert message == constants.credentials['error_message'], "Unexpected message for wrong credentials"

    def test_cancel_button(self, test_setup):
        """
        This method tests if Cancel button returns to previous page
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.click_cancel()
        is_in_screen = login.is_in_login_screen()
        assert is_in_screen, "Did not cancel login screen"

    def test_empty_credentials(self, test_setup):
        """
        This method checks invalid credentials when trying to login with empty credentials
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.click_login()
        message = login.get_error_message()
        assert message == constants.credentials['error_message'], "Unexpected message for wrong credentials"

    def test_valid_login(self, test_setup):
        """
        This method tests a happy happy, trying to login if valid credentials
        :param test_setup: Connection between device under test (DUT) and Appium
        :return: boolean
        """
        home = Home(test_setup)
        home.goto_login_page()
        login = Login(test_setup)
        login.insert_username(constants.credentials['valid_username'])
        login.insert_password(constants.credentials['valid_password_for_valid_username'])
        login.click_login()
        is_logged = login.is_logged()
        if is_logged:
            assert True
        else:
            assert False
