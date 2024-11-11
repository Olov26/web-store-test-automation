from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.common.exceptions import ElementClickInterceptedException
import time


class Laptop_computers(Base):

    def __init__(self, driver):
        super().__init__(driver)


    """Локаторы страницы Ноутбуки и компьютеры"""

    laptop_select = "(//span[@class='app-catalog-pt72uc e66p2eb0'])[1]" #локатор для раздела Ноутбуки
    laptop_title = "//h1[@class='elbnj820 eml1k9j0 app-catalog-kfo60a e1gjr6xo0']" #локатор для заголовка "Ноутбуки"

    """Getters"""

    def get_laptop_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_select)))

    def get_laptop_title(self):
        """Ждет, когда заголовок Ноутбуков станет видимым, и возвращает его текст"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.laptop_title)))

    """Actions"""

    def click_laptop_select(self):
        """Клик на раздел Ноутбуки с обработкой перехваченного клика"""
        try:
            self.get_laptop_select().click()  # Обычный клик по разделу "Ноутбуки"
            print("Клик на раздел Ноутбуки успешен!")
        except ElementClickInterceptedException:
            print("Обычный клик не сработал, выполняется JavaScript-клик.")
            self.driver.execute_script("arguments[0].click();", self.get_laptop_select())
        time.sleep(2)

    """Methods"""

    def open_laptop_select(self):
        """Открывает раздел 'Ноутбуки' на странице 'Ноутбуки и компьютеры' и проверяет заголовок"""
        self.scroll_to()  # Прокрутка страницы вниз
        self.click_laptop_select()  # Клик по разделу "Ноутбуки"
        self.get_current_url() # получение и вывод текущей url
        self.assert_word(self.laptop_title, "Ноутбуки")  # Проверка заголовка страницы
        print("Успешный переход в раздел Ноутбуки")


