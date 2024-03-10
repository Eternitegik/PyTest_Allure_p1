import time
import allure
import re
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class InventoryPage(BasePage):

    PAGE_URL = Links.INVENTORY

    MENU = ('xpath', '//div[@class="bm-menu-wrap"]')
    OPEN_MENU = ('xpath', '//button[@id="react-burger-menu-btn"]')
    CLOSE_MENU = ('xpath', '//button[@id="react-burger-cross-btn"]')

    INVENTORY_LIST = ('xpath', '//div[@class="inventory_item"]')
    ADD_TO_CART = ('xpath', '(//div[@class="inventory_item"])[1]//button')
    SHOPPING_CART_CONTAINER = ('xpath', '//div[@id="shopping_cart_container"]')
    SHOPPING_CART_BADGE = (
        'xpath', '//div[@id="shopping_cart_container"]//span')

    @allure.step('Проверка что меню открыто')
    def menu_is_open(self):
        '''Возвращает True если меню открыто'''
        try:
            self.fast_wait.until(
                EC.visibility_of_element_located(self.CLOSE_MENU))
            return True
        except TimeoutException:
            return False

    @allure.step('Открытие меню')
    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.OPEN_MENU)).click()

        element = self.wait.until(EC.visibility_of_element_located(self.MENU))
        time.sleep(self.get_time_sleep(element))

    @allure.step('Закрытие меню')
    def close_menu(self):
        element = self.wait.until(EC.visibility_of_element_located(self.MENU))

        self.wait.until(EC.element_to_be_clickable(self.CLOSE_MENU)).click()

        time.sleep(self.get_time_sleep(element))

    def check_text_item_btn(self, value):
        '''Проверяет соответствует ли надпись введенному значению'''
        with allure.step(f'Проверка что текст кнопки в карточке предмета равен: "{value}"'):
            self.wait.until(EC.text_to_be_present_in_element(
                self.ADD_TO_CART, value))

    @allure.step('Нажатие на кнопку добавления, удаления предмета')
    def click_btn_add_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()

    def check_shopping_cart_badge(self, count=0):
        '''Если count=0, то будет проверенно на наличие бейджа.
            Если при "0" бейд есть, то будет ошибка.'''
        if count == 0:
            with allure.step(f'Проверка что у корзины нет бейджа'):
                try:
                    self.fast_wait.until(EC.visibility_of_element_located(
                        self.SHOPPING_CART_BADGE))
                    assert False
                except TimeoutException:
                    assert True
        else:
            with allure.step(f'Проверка что у корзины есть бейдж со значением: "{count}"'):
                self.wait.until(EC.text_to_be_present_in_element(
                    self.SHOPPING_CART_BADGE, str(count)))

    def get_time_sleep(self, element):
        match = re.search(r'transition:\s*all\s*(\d+(?:\.\d+)?)s',
                          element.get_attribute("style"))
        return float(match.group(1)) + 0.1
