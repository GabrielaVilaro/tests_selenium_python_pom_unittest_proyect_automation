"""Tests de la page principan de la página automationpractice.com"""

from selenium import webdriver
from pages.page_index import PageIndex
from pages.page_results import ResultCases
from pages.page_buy import PageBuy
import unittest
from pages.base_page import BasePage

__pdoc__ = {}
__pdoc__["TestSearchCases"] = False


class TestSearchCases(unittest.TestCase):
    """Método con las pre-condiciones"""

    def setUp(self):
        self.basePage = BasePage()
        self.driver = webdriver.Chrome(self.basePage.driver)
        self.driver.get(self.basePage.base_url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.resultPage = ResultCases(self.driver)
        self.buyPage = PageBuy(self.driver)

    def test_search_no_element(self):
        """ ##Test #1 Este tests busca un elemento inválido y verifica que la página
        devuelva un mensaje de error error"""

        self.indexPage.search('Manzana')
        self.assertEqual(self.resultPage.get_text(), 'No results were found for your search "Manzana"')

    def test_search_element_valid(self):
        """ ##Test #2
         Este tests busca un elemento válido y verifica que aparezca correctamente el nombre del elemento"""

        self.indexPage.search('Dress')
        self.assertTrue('DRESS' in self.resultPage.return_section_title())

    def test_search_element_valid_two(self):
        """##Test #3 Este tests busca un
         elemento válido y verifica que aparezca correctamente el nombre del elemento"""

        self.indexPage.search('T-Shirt')
        self.assertTrue('T-SHIRT' in self.resultPage.return_section_title())

    def test_button_orange(self):
        """##Test #4
        Este tests busca un elemento, elige el color naranja, agrega 8 y verifica que el número coincida"""

        self.indexPage.search('T-Shirt')
        self.resultPage.click_color()
        self.buyPage.push_quantity('5')
        self.buyPage.add_elements(3)
        number_of_elements = self.buyPage.get_number_of_elements()
        self.assertEqual(number_of_elements, '8')

    def test_list_product_selection(self):
        """##Test #5 Este tests toma diferentes valores de la lista de métodos
        de filtrado de una búsqueda"""

        self.indexPage.search('T-Shirt')
        self.resultPage.product_list_by_select('Product Name: A to Z')
        self.resultPage.product_list_by_value('reference:desc')
        self.resultPage.product_list_by_index(3)

    def test_check_phone_number(self):
        """##Test #6 Este tests checkea el número de teléfono de la página"""

        phone_number = self.indexPage.return_phone_number_of_banner()
        self.assertEqual(phone_number, '0123-456-789')

    ''' Método con las post-condiciones'''

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
