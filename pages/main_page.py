import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main(Base):  # класс-потомок класса Base
    """Класс, в котором содержатся локаторы и методы для главной страницы интернет-магазина"""

    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы для главной странице"""
    product_catalog = "(//span[@class='e1pbr73b0 app-catalog-bh6qcy e1dsa0940'])[2]"   # локатор для раздела Каталог товаров

    """Getters"""
    def get_product_catalog(self):
        """Ожидает, когда элемент товара станет кликабельным и возвращает его"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_catalog)))

    """Actions"""
    def click_product_catalog(self):
        """Клик на раздел Каталог товаров"""
        try:
            self.get_product_catalog().click()
            print("Click Product Catalog")
        except Exception as error_message:
            print(f"Failed to click Product Catalog: {error_message}")

        time.sleep(2)

    """Methods"""

    def open_product_catalog(self):
        """Открываем каталог товаров на главной странице"""
        self.click_product_catalog()  # клик на каталог товаров
        self.get_current_url()  # получение и вывод текущей url
        catalog_title_xpath = "//div[@data-meta-name='CatalogMenuDesktopLayout__title']" #сверяем название заголовка
        self.assert_word(catalog_title_xpath, "Каталог")







