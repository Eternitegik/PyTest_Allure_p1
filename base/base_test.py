import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class BaseTest:

    data: Data

    login_page: LoginPage
    inventory_page: InventoryPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()

        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.inventory_page = InventoryPage(driver)

    def fast_authorization(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.USER_LOGIN)
        self.login_page.enter_password(self.data.USER_PASSWORD)
        self.login_page.click_login_btn()
