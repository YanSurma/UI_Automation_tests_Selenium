from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
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
        item_price = self.find(*loc.ITEM_PRICE)
        item_banner = self.find(*loc.ITEM_BANNER)
        actions.move_to_element(item_banner).perform()
        add_button = self.find(*loc.ADD_BUTTON)
        add_button.click()
        page_item_price = self.find(*loc.ITEM_PRICE)
        assert item_price.text == page_item_price.text

    def add_item_to_compare(self):
        actions = ActionChains(self.driver)
        self.scroll_page(0, 500)
        item_name = self.find(*loc.ITEM_NAME).text
        item_banner = self.find(*loc.ITEM_BANNER)
        actions.move_to_element(item_banner).perform()
        compare_button = self.find(*loc.COMPARE_BUTTON)
        compare_button.click()
        return item_name

    def check_compare_alert(self, product_name):
        compare_alert = self.find(*loc.COMPARE_ALERT)
        assert f'You added product {product_name}' in compare_alert.text

    def check_item_name_on_item_page(self, text):
        item_page_name = self.find(*loc.ITEM_PAGE_NAME)
        assert item_page_name.text == text
