from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.malmstein.yahnac',
            'appActivity': 'com.malmstein.yahnac.login.LoginActivity'
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
