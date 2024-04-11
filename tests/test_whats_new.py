def test_check_header_text_is(whats_new):
    whats_new.open_page(whats_new.page_url)
    whats_new.check_header_title_is("What's New")
