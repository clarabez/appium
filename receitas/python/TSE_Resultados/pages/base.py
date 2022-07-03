from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.resultados_locators import ResultadosLocators


class Base(object):
    def __init__(self, drive):
        self.drive = drive

    def find_element(self, element):
        value = WebDriverWait(self, 30).until(EC.presence_of_element_located((
            element
        )))
        return value

    def is_is_home_screen(self):
        resultados = Base.find_element(self.drive, ResultadosLocators.EXPRESSION_SELECIONE)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True
