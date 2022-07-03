from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocators(object):
    USERNAME = (MobileBy.ID, 'com.malmstein.yahnac:id/login_username')
    PASSWORD = (MobileBy.ID, 'com.malmstein.yahnac:id/login_password')
    LOGIN_BUTTON = (MobileBy.ID, 'com.malmstein.yahnac:id/login_login')
    LOGIN_CANCEL_BUTTON = (MobileBy.ID, 'com.malmstein.yahnac:id/login_cancel')
