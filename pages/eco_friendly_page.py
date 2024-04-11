from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from trio import sleep

from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def sort_items_by_value(self, value):
        select_drop_down = Select(self.find(*loc.SELECT_DROP_DOWN))
        select_drop_down.select_by_value(value)

    def add_item_by_link(self):
        actions = ActionChains(self.driver)
        self.scroll_page(0, 500)
        item_banner = self.find(*loc.ITEM_BANNER)
        actions.move_to_element(item_banner).perform()
        add_link = self.find(*loc.ADD_LINK)
        add_link.click()

    def add_item_by_button(self):
        actions = ActionChains(self.driver)
        self.scroll_page(0, 500)
        item_banner = self.find(*loc.ITEM_BANNER)
        actions.move_to_element(item_banner).perform()
        add_button = self.find(*loc.ADD_BUTTON)
        add_button.click()

    def add_item_to_compare(self):
        actions = ActionChains(self.driver)
        self.scroll_page(0, 500)
        item_name = self.find(*loc.ITEM_NAME).text
        item_banner = self.find(*loc.ITEM_BANNER)
        actions.move_to_element(item_banner).perform()
        compare_button = self.find(*loc.COMPARE_BUTTON)
        compare_button.click()

    def check_compare_alert(self, product_name):
        compare_alert = self.find(*loc.COMPARE_ALERT)
        print(compare_alert.text)
        assert compare_alert.text == f'You added product {product_name} to the comparison list.'

    def check_item_name_on_item_page(self, text):
        item_page_name = self.find(*loc.ITEM_PAGE_NAME)
        print(item_page_name.text)
        assert item_page_name.text == text
