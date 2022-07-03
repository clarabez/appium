import pytest
from selenium import webdriver
from setup import DeviceID

DeviceName = DeviceID


@pytest.fixture(scope='class')
def test_setup():
    """
    Setup functionality to start connection between Appium and our device under test (DUT)
    :return: connection
    """
    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/Users/BEZERRA/PycharmProjects/HackerNews/setup/apks/Yahnac.apk'
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()
