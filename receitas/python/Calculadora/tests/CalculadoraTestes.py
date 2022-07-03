import unittest
from pageobjects.Calc import Calculator
from webdriver.Webdriver import Driver


class CalculadoraTestes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_soma(self):
        calculadora = Calculator(self.driver)
        calculadora.somando(1, 2)

    def test_multiplicacao(self):
        calculadora = Calculator(self.driver)
        calculadora.multiplicando(2, 3)

    def tearDown(self):
        self.driver.instance.quit()
