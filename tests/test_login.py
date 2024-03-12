import allure
from base.base_test import BaseTest


@allure.feature("Проверка страницы авторизации")
@allure.story("Authorization")
class TestLogin(BaseTest):

    @allure.title("Проверка на успешную авторизацию")
    @allure.severity("Critical")
    def test_authorization(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.USER_LOGIN)
        self.login_page.enter_password(self.data.USER_PASSWORD)
        self.login_page.click_login_btn()
        self.inventory_page.is_opened()
