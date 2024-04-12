import allure


@allure.feature('Positive run')
def test_open_women_banner(sale_page):
    sale_page.open_page(sale_page.page_url)
    sale_page.open_women_promo_banner()
    sale_page.check_header_title_is('Women Sale')


@allure.feature('Positive run')
def test_open_women_promo_banner(sale_page):
    sale_page.open_page(sale_page.page_url)
    sale_page.open_men_promo_banner()
    sale_page.check_header_title_is('Men Sale')


@allure.feature('Positive run')
def test_open_jackets_section(sale_page):
    sale_page.open_page(sale_page.page_url)
    sale_page.open_jackets_section()
    sale_page.check_header_title_is('Jackets')
