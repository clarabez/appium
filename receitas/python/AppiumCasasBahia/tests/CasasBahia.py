import unittest
import time
from webdriver.webdriver import Driver
from pageobjects.CasasBahiaHome import CasasBahiaHome, Product


class CasasBahiaApp(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    # def test_Produtos(self):
    #     launch = CasasBahiaHome(self.driver)
    #     launch.go_produtos()

    def tearDown(self):
        self.driver.instance.quit()

    def test_two(self):
        launch = Product(self.driver)
        launch.go_produtos()

    def test_three(self):
        launch = CasasBahiaHome(self.driver)
        launch.go_carrinho

    def test_four(self):
        launch = CasasBahiaHome(self.driver)
        launch.go_conta
