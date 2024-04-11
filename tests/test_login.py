def test_login_user(customer_login):
    customer_login.open_page(customer_login.page_url)
    customer_login.check_header_title_is('Customer Login')
    customer_login.fill_login_form(customer_login.user_email, customer_login.user_password)
    customer_login.check_header_title_is('My Account')
    customer_login.check_auth_account_data(customer_login.user_name, customer_login.user_email)


def test_login_non_existent_user(customer_login):
    customer_login.open_page(customer_login.page_url)
    customer_login.fill_login_form('test@test.com', 'q1w2e3r4')
    customer_login.check_error_alert_text_is()


def test_login_user_with_empty_email(customer_login):
    customer_login.open_page(customer_login.page_url)
    customer_login.check_header_title_is('Customer Login')
    customer_login.fill_login_form("", customer_login.user_password)
    customer_login.check_for_email_error()


def test_login_user_with_empty_password(customer_login):
    customer_login.open_page(customer_login.page_url)
    customer_login.check_header_title_is('Customer Login')
    customer_login.fill_login_form(customer_login.user_email, "")
    customer_login.check_for_password_error()
