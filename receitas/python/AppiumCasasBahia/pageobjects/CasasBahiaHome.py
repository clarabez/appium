import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy


class CasasBahiaHome:
    def __init__(self, driver):
        self.driver = driver
        self.produtos = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ID, 'com.novapontocom.casasbahia:id/tabProduct'
        )))
        self.carrinho = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located(
            MobileBy.ID, 'com.novapontocom.casasbahia:id/tabCart'
        ))

        self.conta = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ID, 'ccom.novapontocom.casasbahia:id/tabAccount'
        )))

        self.home = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ID, 'com.novapontocom.casasbahia:id/tabHome'
        )))

    def go_produtos(self):
        self.produtos.click()

    def go_carrinho(self):
        self.carrinho.click()

    def go_conta(self):
        self.conta(self)

    def go_home(self):
        self.home.click()


class Product:
    def __init__(self, driver):
        self.driver = driver
        self.tvmenu = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.'
            'widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ViewFlipper/'
            'android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.'
            'widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView'
        )))
        self.produtos = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            MobileBy.ID, 'com.novapontocom.casasbahia:id/tabProduct'
        )))

    def go_tvmenu(self):
        self.produtos.click()
        time.sleep(5)
        tvmenutext = self.tvmenu.text()
        self.tvmenu.click()
        assert tvmenutext == "Test", "Did not achieve screen"

    def go_produtos(self):
        self.produtos.click()
