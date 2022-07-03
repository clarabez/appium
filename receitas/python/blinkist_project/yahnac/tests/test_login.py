import pytest
from appium import webdriver
import time
import unittest
from webdriver.Webdriver import Driver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_login_success(self):
        pass

    def test_login_wrong_password(self):
        pass

    def test_login_empty_field(self):
        pass

    def tearDown(self):
        self.driver.instance.quit()
