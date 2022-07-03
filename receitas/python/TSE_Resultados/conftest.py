import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def test_setup():
    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/Users/bezerra/Documents/apks/Resultados.apk',
        'autoGrantPermissions': True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()
