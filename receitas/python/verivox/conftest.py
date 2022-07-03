import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def test_setup():
    """
    Setup functionality to start connection between Appium and our device under test (DUT)
    :return: connection
    """
    desired_cap = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'appPackage': 'de.verivox.contractmanager',
        'appActivity': 'de.verivox.contractmanager.MainActivity',
        'autoGrantPermissions': True, # Avoid Interruptions from Android permissions
        'uiautomator2ServerInstallTimeout': 10000,
        # 'autoDismissAlerts': True, # Avoid Interruptions from Android Alerts
        # 'autoAcceptAlerts': True # For cookies notification
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--areacode', dest='areacode', default='030',
                     help='Insert your area code')
    parser.addoption('--mbits', dest='mbits', default='100',
                     help='Insert mbits value')


def pytest_generate_tests(metafunc):
    if 'areacode' in metafunc.fixturenames:
        metafunc.parametrize('areacode', [metafunc.config.option.endpoint], scope='session')
    if 'mbits' in metafunc.fixturenames:
        metafunc.parametrize('mbits', [metafunc.config.option.endpoint], scope='session')


@pytest.fixture(scope='session')
def validate_areacode(areacode):
    if isinstance(areacode, int):
        return areacode
    else:
        print('Insert a integer value')


@pytest.fixture(scope='session')
def validate_areacode(mbits):
    if mbits == 11 or 50 or 100 or 250:
        return mbits
    else:
        print('Insert a valid value for mbits')