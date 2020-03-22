import time
from selenium.webdriver.common.by import By
from tests.acceptance.pages.base_page import BasePage


class Homepage(BasePage):

    dismiss_button = (By.CSS_SELECTOR, '#mat-dialog-0 > app-welcome-banner > div > button.mat-focus-indicator.close-dialog.mat-raised-button.mat-button-base.mat-primary')
    cookie_button = (By.LINK_TEXT, 'Me want it!')
    account_link = (By.ID, 'navbarAccount')
    login_link = (By.ID, 'navbarLoginButton')

    @property
    def url(self):
        return super(Homepage, self).url + '/#/'

    def click_dismiss_buttons(self):
        BasePage.wait_for_clickable(self, Homepage.cookie_button)
        BasePage.click(self, Homepage.cookie_button)
        BasePage.click(self, Homepage.dismiss_button)

    def click_account_link(self):
        BasePage.click(self, Homepage.account_link)

    def click_login_link(self):
        BasePage.click(self, Homepage.login_link)

    def click_close_products(self, text):
        BasePage.click_exact_text(self, text)
        BasePage.click_close_button(self)
        time.sleep(2)