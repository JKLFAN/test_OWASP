from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # CONFIG
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://localhost:3000'

    # CLICKS
    def click(self, locator):
        self.driver.find_element(*locator).click()

    # GETS
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_header(self):
        header = self.driver.find_element_by_tag_name('h1').text
        return header

    # INPUT TEXT
    def input_text(self, locator, content):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(content)

    # WAITS
    def wait_for_clickable(self, content):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(content)
        )

    def wait_for_visible(self, content):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(content)
        )




