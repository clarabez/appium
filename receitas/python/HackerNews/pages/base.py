from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def find_element(self, element):
        """
        This method is responsible to find elements (with presence_of_element_located condition)
        :param element: element to be searched
        :return: value of the element
        """
        wait = WebDriverWait(self, 10)
        value = wait.until(EC.presence_of_element_located((
            element
        )))
        return value
