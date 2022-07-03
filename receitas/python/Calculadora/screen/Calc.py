from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.num1 = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/digit_1'
        )))
        self.num2 = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/digit_2'
        )))
        self.result = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/result'
        )))
        self.soma = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/op_add'
        )))
        self.multiplicar = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ID, 'com.android.calculator2:id/op_mul'
        ))
        self.dividir = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ID, 'com.android.calculator2:id/op_div'
        ))
        self.subtrair = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ID, 'com.android.calculator2:id/op_sub'
        ))
        self.igual = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.android.calculator2:id/eq'
        )))


    def clicknumber(self, numero):
        _num = str(numero)
        self.driver.instance.find_element(MobileBy.ID, 'com.android.calculator2:id/digit_' + _num).click()
        # assert _num in self.result.text, 'Resultado no result não é o esperado com o valor inserido'

    def somando(self, num1, num2):
        self.clicknumber(num1)
        self.soma.click()
        self.clicknumber(num2)

        result = sum(num1, num2)
        calcResult = int(self.result.text)
        assert result == calcResult, 'Resultados diferentes para soma'

    def multiplicando(self, num1, num2):
        self.clicknumber(num1)
        self.multiplicar.click()
        self.clicknumber(num2)

        result = num1 * num2
        calcResult = int(self.result.text)
        assert result == calcResult, 'Resultados diferentes para multiplicação'

    def dividindo(self, num1, num2):
        self.clicknumber(num1)
        self.dividir.click()
        self.clicknumber(num2)

        result = num1 / num2
        calcResult = int(self.result.text)
        assert result == calcResult, 'Resultados diferentes para divisão'
