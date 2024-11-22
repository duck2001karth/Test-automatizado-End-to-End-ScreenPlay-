import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tasks.login_page import LoginPage
from tasks.catalog_page import CatalogPage
from tasks.cart_page import CartPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from pyunitreport import HTMLTestRunner 

class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test1_login_success(self):
        """Verifica que un login válido permita acceder a la página principal."""
        login_page = LoginPage()
        self.assertTrue(login_page.init_page(self.driver))
        login_page.enter_credential(self.driver, 'standard_user', 'secret_sauce')
        catalog_page = CatalogPage(self.driver)
        self.assertTrue(catalog_page.is_loaded(), "Catalog page is not loaded")

    def test2_add_product_to_cart(self):
        """Verifica que pueda agregar algun producto al carrito"""
        login_page = LoginPage()
        login_page.add_product_to_cart(self.driver)
        catalog_page = CatalogPage(self.driver)
        self.assertTrue(catalog_page.is_loaded(), "Catalog page is not loaded")

    def test3_goto_cart_page(self):
        """Verifica que pueda navegar en el carrito de compras"""
        login_page = LoginPage()
        login_page.navigate_to_cart(self.driver)
        cart_page = CartPage(self.driver)
        self.assertTrue(cart_page.is_loaded(), "Failed to load cart page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Pruebas de Testing'))
