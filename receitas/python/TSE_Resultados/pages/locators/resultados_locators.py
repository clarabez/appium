from appium.webdriver.common.mobileby import MobileBy


class ResultadosLocators(object):
    BTN_PROX = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Próximo\")')
    BTN_ENTENDI = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Entendi\")')
    BTN_LI_ACEITO = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Li\")')
    EXPRESSION_SELECIONE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(\"Selecione\")')
