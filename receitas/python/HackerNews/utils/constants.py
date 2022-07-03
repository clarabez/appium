from appium.webdriver.common.mobileby import MobileBy

"""
File to store general constant information 
"""

credentials = {
    'valid_username': 'clarinhabez',
    'valid_password_for_valid_username': 'cloud123',
    'invalid_username': 'cla',
    'invalid_password': '123',
    'error_message': 'Please enter valid credentials'
}

LOGIN_ERROR_MESSAGE = MobileBy.ID, 'com.malmstein.yahnac:id/login_error_label'
