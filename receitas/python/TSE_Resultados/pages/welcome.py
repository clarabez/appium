from appium.webdriver.common.touch_action import TouchAction
import time
from pages.locators.resultados_locators import ResultadosLocators
from pages.base import Base
from pages.home import Home


class Initial(Base):
    def realizar_fluxo_inicial(self):
        btn_prox = Base.find_element(self.drive, ResultadosLocators.BTN_PROX)
        btn_prox.click()
        btn_entendi = Base.find_element(self.drive, ResultadosLocators.BTN_ENTENDI)
        btn_entendi.click()
        TouchAction(self.drive).press(x=487, y=1538).move_to(x=497, y=515).release().perform()
        btn_li_aceito = Base.find_element(self.drive, ResultadosLocators.BTN_LI_ACEITO)
        btn_li_aceito.click()

