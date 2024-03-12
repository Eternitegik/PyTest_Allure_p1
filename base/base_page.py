import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.fast_wait = WebDriverWait(driver, 1)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'Page {self.PAGE_URL} is open'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def element_clickable(self, xpath):
        return self.wait.until(EC.element_to_be_clickable(xpath))

    def visibility_element(self, xpath):
        return self.wait.until(EC.visibility_of_element_located(xpath))

    def visibility_all_elements(self, xpath):
        return self.wait.until(EC.visibility_of_all_elements_located(xpath))

    def text_to_be_present_in_element(self, xpath, text):
        return self.wait.until(EC.text_to_be_present_in_element(xpath, str(text)))
