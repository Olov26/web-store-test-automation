
"""Базовый класс с универсальными методами"""
from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str): # если нужно использовать на других страницах
        """Открывает указанную страницу"""
        self.driver.get(url)

    def open_main_page(self):
        """Открывает главную страницу Ситилинк"""
        main_url = "https://www.citilink.ru/"
        self.open(main_url)
        print("Главная страница успешно открыта!")

    """Method GET current URL"""

    def get_current_url(self):
        """Получаем текущий URL открытой страницы"""
        get_url = self.driver.current_url
        print("Текущий URL " + get_url)

    """ Method assert word """

    def assert_word(self, xpath, expected_text):
        """Находит элемент по XPath и проверяет, что его текст соответствует ожидаемому"""
        element = self.driver.find_element(By.XPATH, xpath)  # Ищем элемент по переданному XPath
        actual_text = element.text  # Получаем текст элемента
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        print(f"Text matches: {actual_text}")


    """ method page scroll"""
    def scroll_to(self):
        """Прокрутка происходит на 200 пикселей по вертикали, начиная с верхней части страницы"""
        self.driver.execute_script("window.scrollTo(0, 200)")
        print("Прокрутка страницы выполнена успешно")






