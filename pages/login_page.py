import allure
from base.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):

    PAGE_URL = Links.HOST
    USERNAME_FIELD = ('xpath', '//input[@name="user-name"]')
    PASSWORD_FIELD = ('xpath', '//input[@name="password"]')
    SUBMIT_BTN = ('xpath', '//input[@name="login-button"]')

    @allure.step('Заполнение поля "Username"')
    def enter_login(self, login):
        self.element_clickable(self.USERNAME_FIELD).send_keys(login)

    def enter_password(self, password):
        with allure.step(f'Заполнение поля "Password"'):
            self.element_clickable(self.PASSWORD_FIELD).send_keys(password)

    @allure.step('Нажатие на кнопку "Login"')
    def click_login_btn(self):
        self.element_clickable(self.SUBMIT_BTN).click()
