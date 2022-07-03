from pages.base import Base
from pages.locators.resultados_locators import ResultadosLocators
from selenium.common.exceptions import NoSuchElementException


class Home(Base):
    def is_is_home_screen(self):
        resultados = Base.find_element(self.drive, ResultadosLocators.BTN_RESULTADOS)
        try:
            resultados
        except NoSuchElementException:
            return False
        return True
