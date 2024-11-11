import time

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Laptop_finish(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы страницы конечной страницы Ноутбуки"""

    price_field = "(//input[@name='input-max'])[2]" # локатор для поля ввода максимальной цены
    check_box_self_pickup = "e1lvuglt0.app-catalog-owd97p.e1paenzp0" # локатор для чек-бокса "Доступен самовывоз"
    radio_button_rating = "//input[@name='rating.4.5']" # локатор для радиобаттона "Оценка товара по отзывам"
    # локатор для радиобаттона рейтинг от 4.5 по CSS selector
    radio_button_rating_click = "#__next > div > main > section > div.app-catalog-i9gxme.e1r05wpd0 > div > div > section > div.et5jpcw0.app-catalog-8y4mwr.e1loosed0 > div > div > div.elzy9qw0.app-catalog-1q62o3l.e15of8sa0 > div.app-catalog-1fvvpk9.e1tpjdq30 > div > div.em0tyie0.app-catalog-1tn5u6r.e1hyqf8x0 > div.en1uwyl0.app-catalog-ypf6rj.ex1z6690 > div:nth-child(6) > div.app-catalog-18f9ifi.ee2gm9s0 > div > div > div > div > div:nth-child(2) > div"
    # локатор для кнопки добавить в корзину
    add_to_cart = "#__next > div > main > section > div.app-catalog-i9gxme.e1r05wpd0 > div > div > section > div.e12wdlvo0.app-catalog-1r4e8wl.e1loosed0 > div.ehanbgo0.app-catalog-1w7tb29.e1loosed0 > div:nth-child(4) > div > div.app-catalog-rhd9cx.e8kvwwz0 > div.app-catalog-817h00.ean5xps0 > div.app-catalog-fls229.e1sk5tid0 > div.fresnel-container.fresnel-greaterThanOrEqual-mobileL > button"
    def get_price_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_field)))
    def get_check_box_self_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, self.check_box_self_pickup)))
    def get_radio_button_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.NAME, self.radio_button_rating)))
    def set_radio_button_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.radio_button_rating_click)))
    def get_add_to_cart(self):
        """Ожидает, когда элемент товара станет кликабельным и возвращает его"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.add_to_cart)))

    """Actions"""

    def set_price_limit(self, price):
        """Установка предельной суммы заказа"""
        price_field = self.get_price_field()
        price_field.click()  # Устанавливаем фокус на поле
        price_field.clear()  # Очищаем поле

        # Вводим сумму
        price_field.send_keys(price)
        print(f"Сумма заказа установлена до {price}")

    def click_check_box(self):
        """Устанавливает чекбокс для самовывоза"""
        self.get_check_box_self_pickup().click()


    def scroll_to_element(self, element_locator):
        """Прокрутка страницы до конкретного элемента"""
        # Ждём, пока элемент появится на странице
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, element_locator)))
        # Скроллим до элемента
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_radio_button_rating(self):
       self.set_radio_button_rating().click() #клик по радиобаттону рейтинг 4.5


    def click_add_to_cart(self):
        self.get_add_to_cart().click() #клик по кнопке Добавить в корзину
        print("Клик в корзину выполнен успешно")

    """Methods"""

    def set_order_limit(self):
        """Прокрутка страницы к полю ввода цены и установка лимита суммы заказа до 90000"""
        price_field = self.get_price_field()  # Получаем элемент поля для цены
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",price_field)  # Прокручиваем до поля цены
        WebDriverWait(self.driver, 30).until(EC.visibility_of(price_field))  # Ждем, пока поле станет видимым
        time.sleep(2)
        self.set_price_limit(90000)  # Устанавливаем лимит суммы заказа


    def set_check_box(self):
        self.click_check_box() #клик по чекбоксу Доступен самовывоз
        print("Выбран чекбокс Доступен самовывоз")

    def set_radio_button(self):
        self.scroll_to_element(self.radio_button_rating)  # Прокручиваем до радиобаттона
        self.click_radio_button_rating()

        print("Выбран радиобаттон для рейтинга 4.5")

        time.sleep(2)

    def select_add_to_cart(self):
        self.click_add_to_cart()
        print("Клик по кнопке В корзину")

        time.sleep(2)






