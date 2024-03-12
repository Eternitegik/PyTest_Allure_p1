from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CartPage(BasePage):

    PAGE_URL = Links.CART

    CART_LIST = ('xpath', '//div[@class="cart_item"]')
    CART_REMOVE_BTN = ('xpath', '//div[@class="cart_item"]//button')

    def check_cart_list_not_null(self):
        self.visibility_all_elements(self.CART_LIST)

    def get_count_cart_list(self):
        try:
            return len(self.fast_wait.until(EC.visibility_of_all_elements_located(self.CART_LIST)))
        except TimeoutException:
            return 0

    def remove_element_in_cart(self):
        self.element_clickable(self.CART_REMOVE_BTN).click()
