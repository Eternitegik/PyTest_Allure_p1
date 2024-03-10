import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.HOST
    USERNAME_FIELD = ('xpath', '//input[@name="user-name"]')
    PASSWORD_FIELD = ('xpath', '//input[@name="password"]')
    SUBMIT_BTN = ('xpath', '//input[@name="login-button"]')

    @allure.step('Заполнение поля "Username"')
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(
            self.USERNAME_FIELD)).send_keys(login)

    @allure.step('Заполнение поля "Password"')
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(
            self.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Нажатие на кнопку "Login"')
    def click_login_btn(self):
        self.wait.until(EC.element_to_be_clickable(
            self.SUBMIT_BTN)).click()
