from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import sale_page_locator as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def open_women_promo_banner(self):
        women_banner = self.find(*loc.WOMEN_BANNER)
        women_banner.click()

    def open_men_promo_banner(self):
        men_banner = self.find(*loc.MEN_BANNER)
        men_banner.click()

    def open_jackets_section(self):
        jackets_section = self.find(*loc.JACKETS_SECTION)
        jackets_section.click()
