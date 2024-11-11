import time

from base.base_class import Base

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import unicodedata
def normalize_text(text):
    text = unicodedata.normalize("NFKD", text).strip().replace('\u200b', '').replace('\u00a0', ' ')
    return ' '.join(text.split())  # Убирает лишние пробелы

class Cart(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы страницы Корзина"""
    # заголовок корзина
    cart_title = "#__next > div > main > div.css-8d6fcv.epxd7oz0 > div.css-126r7ui.e1i5m9cv0 > div > div > span"
    # название товара в корзине
    cart_product_name = "#__next > div > main > div.css-8d6fcv.epxd7oz0 > div.e412wun0.css-1gk1vav.e164boj10 > section > div.e17gms870.css-1hx51my.e1loosed0 > div.css-8atqhb.e1wttw970 > div > div > div.css-1iwyt7x.ee69zgt0 > div > a > span"
    # цена товара в корзине
    cart_product_price = "#__next > div > main > div.css-8d6fcv.epxd7oz0 > div.e412wun0.css-1gk1vav.e164boj10 > section > div.e12wdlvo0.css-p5y6it.e1loosed0 > div > div.css-8gvgvd.eyoh4ac0 > div:nth-child(1) > div:nth-child(1) > div.css-0.e1307olx0 > div > span > span > span.e1j9birj0.e106ikdt0.css-1spb733.e1gjr6xo0"
    # кнопка перейти к оформлению
    button_go_to_checkout = "#__next > div > main > div.css-8d6fcv.epxd7oz0 > div.e412wun0.css-1gk1vav.e164boj10 > section > div.e12wdlvo0.css-p5y6it.e1loosed0 > div > div.css-8gvgvd.eyoh4ac0 > div:nth-child(1) > div:nth-child(1) > div.css-0.eqwt6oe0 > button"

    """Getters"""

    def get_cart_title(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cart_title)))

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cart_product_name)))

    def get_cart_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cart_product_price)))

    def get_button_go_to_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_go_to_checkout)))

    """Methods"""

    def verify_cart_title(self, expected_title):
        """Проверяем, что заголовок в корзине совпадает с ожидаемым значением"""
        actual_title = self.get_cart_title().text
        assert actual_title == expected_title, f"Заголовок не совпадает: ожидается '{expected_title}', найдено '{actual_title}'"
        print("Заголовок в корзине совпадает")

        time.sleep(2)

    def verify_cart_product_details(self, expected_cart_name, expected_cart_price):
        """Проверяем, что название товара и его цена вкорзине совпадают с ожидаемыми значениями"""
        actual_cart_name = normalize_text(self.get_cart_product_name().text)
        actual_cart_price = normalize_text(self.get_cart_product_price().text)
        expected_cart_name = normalize_text(expected_cart_name)
        expected_cart_price = normalize_text(expected_cart_price)

        assert actual_cart_name == expected_cart_name, f"Название товара не совпадает: ожидается '{expected_cart_name}', найдено '{actual_cart_name}'"
        print("Название в корзине совпадает")
        assert actual_cart_price == expected_cart_price, f"Цена товара не совпадает: ожидается '{expected_cart_price}', найдено '{actual_cart_price}'"
        print("Цена в корзине совпадает")
        time.sleep(2)

    def click_button_go_to_checkout(self):
        self.get_button_go_to_checkout().click()
        print("Клик на кнопку Перейти к оформлению")
        time.sleep(2)

    # на этом тест заканчивается, т.к дальнейшие действия требуют авторизации




