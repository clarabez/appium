from appium import webdriver


class Driver:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Appium1",
            "appPackage": "com.novapontocom.casasbahia",
            "appActivity": "br.com.viavarejo.feature.home.HomeActivity"
        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
