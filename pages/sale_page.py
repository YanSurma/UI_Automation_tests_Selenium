from time import sleep

from pages.base_page import BasePage
from pages.locators import sale_page_locator as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def open_all_menu_sections(self):
        menu_sections = self.find_all(*loc.MENU_SECTIONS)
        for section in menu_sections:
            section_name = section.text
            section.click()
            self.check_header_title_is(section_name)
            self.driver.back()
            self.check_header_title_is("Sale")
