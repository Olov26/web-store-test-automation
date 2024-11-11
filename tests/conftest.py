
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Раскрываем окно браузера на весь экран
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver  # Возвращаем драйвер для использования в тестах
    driver.quit()  # Закрываем браузер после завершения тестов
