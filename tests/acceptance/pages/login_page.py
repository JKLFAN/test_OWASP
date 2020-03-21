import time
from selenium.webdriver.common.by import By
from tests.acceptance.pages.base_page import BasePage


class LoginPage(BasePage):

    expected_title = 'Login'
    new_customer = (By.LINK_TEXT, 'Not yet a customer?')
    google_login = (By.ID, 'loginButtonGoogle')

    @property
    def url(self):
        return super(LoginPage, self).url + '/#/login'

    def click_new_customer(self):
        time.sleep(4)
        BasePage.click(self, LoginPage.new_customer)

    def assert_header(self):
        BasePage.wait_for_visible(self, LoginPage.google_login)
        actual_title = BasePage.get_header(self)
        assert actual_title == LoginPage.expected_title

    def assert_url(self):
        expected_url = LoginPage(self.driver).url
        assert BasePage.get_current_url(self) == expected_url

