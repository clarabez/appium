from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocators(object):
    """
    This class contains all the defined elements for login page
    """
    USERNAME = (MobileBy.ID, 'com.malmstein.yahnac:id/login_username')
    PASSWORD = (MobileBy.ID, 'com.malmstein.yahnac:id/login_password')
    LOGIN = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.'
                             'widget.DrawerLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/'
                             'android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                             'android.widget.Button')
    LOGIN_BUTTON = (MobileBy.ID, 'com.malmstein.yahnac:id/login_login')
    CONTAINER_BUTTONS = (MobileBy.ID, 'com.malmstein.yahnac:id/login_buttons_container')
    LOGIN_CANCEL_BUTTON = (MobileBy.ID, 'com.malmstein.yahnac:id/login_cancel')
    HAMBURGUER_MENU = (MobileBy.ACCESSIBILITY_ID, 'Navigate up')
    SIGNIN_BTN = (MobileBy.ID, 'com.malmstein.yahnac:id/view_drawer_header_login')
    LOGIN_ERROR_MESSAGE = MobileBy.ID, 'com.malmstein.yahnac:id/login_error_label'
