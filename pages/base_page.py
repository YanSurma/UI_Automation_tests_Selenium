from selenium.webdriver.remote.webdriver import WebDriver
from pages.locators import base_locators as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(f'{self.base_url}{page_url}')
        print()

    def scroll_page(self, x1, x2):
        self.driver.execute_script(f"window.scrollBy({x1}, {x2})")

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_all(self, *locator):
        return self.driver.find_elements(*locator)

    def check_header_title_is(self, title):
        header_title = self.find(*loc.HEADER_TITLE)
        print(header_title.text)
        assert header_title.text == title
