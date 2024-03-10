import time
import allure
from base.base_test import BaseTest


@allure.feature("Проверка страницы магазина")
class TestInventoryPage(BaseTest):

    @allure.title("Проверка открытия меню")
    @allure.severity("Critical")
    def test_open_menu(self):
        self.fast_authorization()

        self.inventory_page.is_opened()
        assert not self.inventory_page.menu_is_open()
        self.inventory_page.open_menu()
        assert self.inventory_page.menu_is_open()
        self.inventory_page.close_menu()
        assert not self.inventory_page.menu_is_open()

    @allure.title("Проверка добавления покупки в корзину")
    @allure.severity("Critical")
    def test_add_purchase_cart(self):
        self.fast_authorization()

        self.inventory_page.check_shopping_cart_badge()
        self.inventory_page.check_text_item_btn("Add to cart")
        self.inventory_page.click_btn_add_cart()
        self.inventory_page.check_text_item_btn("Remove")
        self.inventory_page.check_shopping_cart_badge(1)

        self.inventory_page.click_btn_add_cart()
        self.inventory_page.check_shopping_cart_badge()
        self.inventory_page.check_text_item_btn("Add to cart")
