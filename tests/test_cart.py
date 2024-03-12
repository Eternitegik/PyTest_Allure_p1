import allure
from base.base_test import BaseTest


@allure.feature("Проверка страницы покупок")
@allure.story("Cart")
class TestCart(BaseTest):

    @allure.title("Проверка наличия товаров в корзине")
    @allure.severity("Critical")
    def test_check_cart(self):
        self.fast_authorization()

        self.inventory_page.is_opened()
        self.inventory_page.click_btn_add_cart()
        self.inventory_page.go_shopping_cart()

        self.cart_page.is_opened()
        self.cart_page.check_cart_list_not_null()

    @allure.title("Проверка удаления элемента из корзины")
    @allure.severity("Critical")
    def test_remove_element_in_cart(self):
        self.fast_authorization()

        self.inventory_page.is_opened()
        self.inventory_page.click_btn_add_cart()
        self.inventory_page.go_shopping_cart()

        self.cart_page.is_opened()
        count = self.cart_page.get_count_cart_list()
        count -= 1
        self.cart_page.remove_element_in_cart()
        assert self.cart_page.get_count_cart_list(
        ) == count, 'Количество товаров после удаления не изменилось'
