def test_add_item_by_button_sorting_by_price(eco_page):
    eco_page.open_page(eco_page.page_url)
    eco_page.check_header_title_is('Eco Friendly')
    eco_page.sort_items_by_value("price")
    eco_page.add_item_by_button()


def test_add_item_by_link_sorting_by_position(eco_page):
    eco_page.open_page(eco_page.page_url)
    eco_page.check_header_title_is('Eco Friendly')
    eco_page.sort_items_by_value("position")
    eco_page.add_item_by_link()
    eco_page.check_item_name_on_item_page('Ana Running Short')


def test_add_item_sorting_by_name_to_compare(eco_page):
    eco_page.open_page(eco_page.page_url)
    eco_page.check_header_title_is('Eco Friendly')
    eco_page.sort_items_by_value("name")
    item_name = eco_page.add_item_to_compare()
    eco_page.check_compare_alert(item_name)

