import random
import string
from selenium.webdriver.common.by import By
from tests.acceptance.pages.base_page import BasePage


class RegisterPage(BasePage):

    expected_title = 'User Registration'
    email = By.ID, 'emailControl'
    password = By.ID, 'passwordControl'
    repeatPassword = By.ID, 'repeatPasswordControl'
    securityField = By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-register/div/mat-card/div[2]/div[1]/mat-form-field[1]/div/div[1]/div[3]/mat-select'
    securityQuestion = By.XPATH, '/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span'
    securityAnswer = By.ID, 'securityAnswerControl'
    registerButton = By.ID, 'registerButton'

    @property
    def url(self):
        return super(RegisterPage, self).url + '/#/register'

    def randomString(length=4):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def assert_header(self):
        actual_header = BasePage.get_header(self)
        assert actual_header == RegisterPage.expected_title

    def assert_url(self):
        expected_url = RegisterPage(self.driver).url
        assert BasePage.get_current_url(self) == expected_url

    def enter_details(self):
        randomString = RegisterPage.randomString()
        BasePage.input_text(self, RegisterPage.email, randomString + '@test.com')
        BasePage.input_text(self, RegisterPage.password, 'testtest')
        BasePage.input_text(self, RegisterPage.repeatPassword, 'testtest')
        BasePage.input_text(self, RegisterPage.repeatPassword, 'testtest')
        BasePage.click(self, RegisterPage.securityField)
        BasePage.click(self, RegisterPage.securityQuestion)
        BasePage.input_text(self, RegisterPage.securityAnswer, 'smith')
        BasePage.click(self, RegisterPage.registerButton)


