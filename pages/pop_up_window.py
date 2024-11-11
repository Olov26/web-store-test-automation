from base.base_class import Base

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import unicodedata


def normalize_text(text): # используется, т.к в название товара в двух разных местах одно и тоже название имеет разное кол-во пробелов
    """Эта функция нормализует текст, удаляя лишние пробелы и нежелательные символы.
	•	unicodedata.normalize("NFKD", text) — нормализует строку в формат NFKD (удаляет ненормализованные символы, такие как акценты).
	•	.strip() — удаляет пробелы в начале и в конце строки.
	•	.replace('\u200b', '') — удаляет невидимый символ (Zero Width Space).
	•	.replace('\u00a0', ' ') — заменяет неразрывный пробел на обычный пробел."""

    text = unicodedata.normalize("NFKD", text).strip().replace('\u200b', '').replace('\u00a0', ' ')
    return ' '.join(text.split())  # Убирает лишние пробелы

class Pop_up(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы для всплывающего окна"""
    #заголовок
    product_title = "body > div.PopupScrollContainer > div > div > div > div > div > div.app-catalog-11xlm83.e1mrirr40 > span"
    # название товара
    product_name = "body > div.PopupScrollContainer > div > div > div > div > div > div.app-catalog-10hz06r.e15vok0l0 > div > div.app-catalog-w6xdhd.ezol2u00 > div.app-catalog-hdphih.eu1unfa0"
    # цена
    product_price = "body > div.PopupScrollContainer > div > div > div > div > div > div.app-catalog-10hz06r.e15vok0l0 > div > div.app-catalog-19i70pr.e1wy53ig0 > div.app-catalog-qfdd9t.e1rmqbmc0 > span > span > span > span.e1j9birj0.e106ikdt0.app-catalog-56qww8.e1gjr6xo0"
    # кнопка Перейти в корзину
    go_to_cart = "body > div.PopupScrollContainer > div > div > div > div > div > div.app-catalog-1m535y2.e1jliu4a0 > a > button"

    """Getters"""
    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.product_title)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.product_price)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.go_to_cart)))


    """Methods"""

    def verify_popup_title(self, expected_title):
        """Проверяем, что заголовок всплывающего окна совпадает с ожидаемым значением"""
        actual_title = self.get_product_title().text
        assert actual_title == expected_title, f"Заголовок не совпадает: ожидается '{expected_title}', найдено '{actual_title}'"
        print("Заголовок совпадает")

    def verify_product_details(self, expected_name, expected_price):
        """Проверяем, что название товара и его цена в всплывающем окне совпадают с ожидаемыми значениями"""
        actual_name = normalize_text(self.get_product_name().text)
        actual_price = normalize_text(self.get_product_price().text)
        expected_name = normalize_text(expected_name)
        expected_price = normalize_text(expected_price)

        assert actual_name == expected_name, f"Название товара не совпадает: ожидается '{expected_name}', найдено '{actual_name}'"
        print("Название совпадает")
        assert actual_price == expected_price, f"Цена товара не совпадает: ожидается '{expected_price}', найдено '{actual_price}'"
        print("Цена совпадает")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Клик на кнопку Перейти в корзину")
