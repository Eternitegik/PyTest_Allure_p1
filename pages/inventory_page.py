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
        # self.wait.until(EC.element_to_be_clickable(self.OPEN_MENU)).click()
        self.element_clickable(self.OPEN_MENU).click()

        # element = self.wait.until(EC.visibility_of_element_located(self.MENU))
        element = self.visibility_element(self.MENU)
        time.sleep(self.get_time_sleep(element))

    @allure.step('Закрытие меню')
    def close_menu(self):
        # element = self.wait.until(EC.visibility_of_element_located(self.MENU))
        element = self.visibility_element(self.MENU)

        # self.wait.until(EC.element_to_be_clickable(self.CLOSE_MENU)).click()
        self.element_clickable(self.CLOSE_MENU).click()

        time.sleep(self.get_time_sleep(element))

    def go_shopping_cart(self):
        # self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_CONTAINER)).click()
        self.element_clickable(self.SHOPPING_CART_CONTAINER).click()

    def check_text_item_btn(self, value):
        with allure.step(f'Проверка что текст кнопки в карточке товара равен: "{value}"'):
            self.wait.until(EC.text_to_be_present_in_element(
                self.ADD_TO_CART, value))

    @allure.step('Нажатие на кнопку добавления, удаления предмета')
    def click_btn_add_cart(self):
        # self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.element_clickable(self.ADD_TO_CART).click()

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
                # self.wait.until(EC.text_to_be_present_in_element(self.SHOPPING_CART_BADGE, str(count)))
                self.text_to_be_present_in_element(
                    self.SHOPPING_CART_BADGE, str(count))

    def get_time_sleep(self, element):
        match = re.search(r'transition:\s*all\s*(\d+(?:\.\d+)?)s',
                          element.get_attribute("style"))
        return float(match.group(1)) + 0.1

    def list_products_not_empty(self):
        # elements = self.wait.until(EC.visibility_of_all_elements_located(self.INVENTORY_LIST))
        elements = self.visibility_all_elements(self.INVENTORY_LIST)
        assert len(elements) != 0

    def check_product_img(self, id=0, img_name=''):
        # element_src = self.wait.until(EC.visibility_of_element_located(('xpath', f'//a[@id="item_{id}_img_link"]/img'))).get_attribute("src")
        element_src = self.visibility_element(
            ('xpath', f'//a[@id="item_{id}_img_link"]/img')).get_attribute("src")
        assert element_src and "/static/media/" in element_src and element_src.endswith(
            ".jpg")
        if img_name:
            assert img_name in element_src, f'Название изображение не соответствует {
                img_name}. ССылка: {element_src}'

    def check_product_description(self, id=0, pr_header='', pr_desc='', pr_price=''):
        START_XPATH = f'//a[@id="item_{id}_title_link"]/parent::div/parent::div'
        LINK = ('xpath', f'//a[@id="item_{id}_title_link"]')
        HEADER = (
            'xpath', f'{START_XPATH}//div[contains(@class,"inventory_item_name")]')
        DESCRIPTION = (
            'xpath', f'{START_XPATH}//div[contains(@class,"inventory_item_desc")]')
        PRICE = (
            'xpath', f'{START_XPATH}//div[contains(@class,"inventory_item_price")]')

        # element_link = self.wait.until(EC.visibility_of_element_located(LINK))
        # element_header = self.wait.until(EC.visibility_of_element_located(HEADER))
        # element_description = self.wait.until(EC.visibility_of_element_located(DESCRIPTION))
        # element_price = self.wait.until(EC.visibility_of_element_located(PRICE))

        element_link = self.visibility_element(LINK)
        element_header = self.visibility_element(HEADER)
        element_description = self.visibility_element(DESCRIPTION)
        element_price = self.visibility_element(PRICE)

        assert element_link.get_attribute('id'), 'Атрибут "id" пуст'
        assert element_header.text, 'Заголовок пуст'
        assert element_description.text, 'Описание пусто'
        assert element_price.text, 'Цена пуста'

        if pr_header:
            assert pr_header in element_header.text, f'Заголовок не совпадает с "{
                pr_header}". Текст: "{element_header.text}"'
        if pr_desc:
            assert pr_desc in element_description.text, f'Описание не совпадает с "{
                pr_desc}". Текст: "{element_header.text}"'
        if pr_price:
            assert pr_price in element_price.text, f'Заголовок не совпадает с "{
                pr_price}". Текст: "{element_header.text}"'
