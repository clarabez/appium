from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self._driver.get(url)

    def find_element(self, element):
        return WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            element
        )))

    def send_keys(self, element, keys):
        self._driver.find_element(element).send_keys(keys)

    def click(self, element):
        self._driver.find_element(*element).click()
