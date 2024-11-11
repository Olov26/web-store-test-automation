from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Catalog(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Локатор страницы Каталог"""


    select_laptop_computer = "/html/body/div[4]/div/div/div/div/div/div[5]/div/div/div[2]/div/div[1]/div/div[1]/div/a[3]/div/span"
    section_title = "//div[@class='app-catalog-ltibc4 ek3njma0']" #локатор для заголовка Ноутбуки и компьютеры

    """Getters"""

    def get_select_laptop_computer(self):
        """Ожидает, когда элемент товара станет кликабельным и возвращает его"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_laptop_computer)))

    def get_section_title(self):
        """Ожидает, когда заголовок Ноутбуки и компьютеры станет видимым"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.section_title)))

    """Actions"""

    def click_laptop_computer(self):
        """Клик на раздел Ноутбуки и компьютеры"""
        self.get_select_laptop_computer().click()
        print("Клик на раздел Ноутбуки и компьютеры успешен!")
        time.sleep(2)

    """Methods"""

    def open_laptop_computer_section(self):
        """Кликает на раздел 'Ноутбуки и компьютеры' и проверяет заголовок"""
        self.click_laptop_computer()  # Клик по разделу "Ноутбуки и компьютеры"
        self.get_current_url()  # Получение текущего URL
        self.assert_word(self.section_title, "Ноутбуки и компьютеры")  # Проверка заголовка страницы
        print("Успешный переход в раздел Ноутбуки и компьютеры")
