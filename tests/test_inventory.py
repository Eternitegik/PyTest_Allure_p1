import allure
from base.base_test import BaseTest


@allure.feature("Проверка страницы товаров")
@allure.story("Inventory")
class TestInventory(BaseTest):

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

    @allure.title("Проверка списка товаров")
    @allure.severity("Critical")
    def test_products_list(self):
        self.fast_authorization()

        self.inventory_page.is_opened()
        self.inventory_page.list_products_not_empty()
        self.inventory_page.check_product_img()
        self.inventory_page.check_product_url_header()
        self.inventory_page.check_product_header()
        self.inventory_page.check_product_description()
        self.inventory_page.check_product_price()

    @allure.title("Проверка добавления покупки в корзину")
    @allure.severity("Critical")
    def test_add_purchase_cart(self):
        self.fast_authorization()

        self.inventory_page.is_opened()
        self.inventory_page.check_shopping_cart_badge()
        self.inventory_page.check_text_item_btn("Add to cart")
        self.inventory_page.click_btn_add_cart()
        self.inventory_page.check_text_item_btn("Remove")
        self.inventory_page.check_shopping_cart_badge(1)

        self.inventory_page.click_btn_add_cart()
        self.inventory_page.check_shopping_cart_badge()
        self.inventory_page.check_text_item_btn("Add to cart")
