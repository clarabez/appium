from appium.webdriver.common.mobileby import MobileBy

class GeneralLocators(object):
    button_dsl = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"DSL\")')
    area_code_field = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    mbit_100 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"100\")')
    button_vergleichen = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"JETZT VERGLEICHEN\")')
    # text_ermittelte_tarife = (MobileBy.ANDROID_UIAUTOMATOR,
    #                           'new UiSelector().textContains(\"Ermittelte Tarife\")')
    button_cookie = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"ALLES AKZEPTIEREN\")')
