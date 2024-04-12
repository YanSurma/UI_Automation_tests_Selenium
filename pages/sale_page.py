import allure

from pages.base_page import BasePage
from pages.locators import sale_page_locator as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Open women banner')
    def open_women_promo_banner(self):
        women_banner = self.find(*loc.WOMEN_BANNER)
        women_banner.click()

    @allure.step('Open men banner')
    def open_men_promo_banner(self):
        men_banner = self.find(*loc.MEN_BANNER)
        men_banner.click()

    @allure.step('Open jacket section')
    def open_jackets_section(self):
        jackets_section = self.find(*loc.JACKETS_SECTION)
        jackets_section.click()
