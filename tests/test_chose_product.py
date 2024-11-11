import time

from pages.cart_page import Cart
from pages.catalog_page import Catalog
from pages.laptop_finish_page import Laptop_finish
from pages.main_page import Main
from pages.laptop_computers_page import Laptop_computers
from pages.pop_up_window import Pop_up


def test_chose_product(browser):
    print("Тест начат")


    mp = Main(browser)
    mp.open_main_page()
    mp.open_product_catalog() # открытие раздела Католог

    sc = Catalog(browser)
    sc.open_laptop_computer_section() # выбор раздела Ноутбуки и компьютеры и проверка заголовка

    lc = Laptop_computers(browser)
    lc.open_laptop_select()  # Открытие раздела "Ноутбуки" и проверка заголовка

    lf = Laptop_finish(browser)
    lf.set_order_limit()  # Устанавливаем лимит суммы до 60000
    lf.set_check_box()  # Устанавливаем чекбокс самовывоза
    lf.set_radio_button()  # Устанавливаем радиобаттон для рейтинга 4.5

    lf.select_add_to_cart()

    pw = Pop_up(browser)
    pw.verify_popup_title("Товар добавлен в корзину")
    pw.verify_product_details(expected_name='Ноутбук Huawei MateBook D 14 14", 2024, IPS, Intel Core i5 12450H 2ГГц, 8-ядерный, 16ГБ LPDDR4x, 512ГБ SSD,  Intel UHD Graphics, без операционной системы, серый космос [53013xet]', expected_price='62 990')

    pw.click_go_to_cart()

    cp = Cart(browser)
    cp.verify_cart_title("Корзина")
    cp.verify_cart_product_details(expected_cart_name='Ноутбук Huawei MateBook D 14 14", 2024, IPS, Intel Core i5 12450H 2ГГц, 8-ядерный, 16ГБ LPDDR4x, 512ГБ SSD,  Intel UHD Graphics, без операционной системы, серый космос [53013xet]', expected_cart_price='62 990')

    cp.click_button_go_to_checkout()

    print("Тест завершен!")

