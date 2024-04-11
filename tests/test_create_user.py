def test_create_user(create_account):
    create_account.open_page(create_account.page_url)
    create_account.check_header_title_is('Create New Customer Account')
    first_name, last_name, email = create_account.fill_auth_form()
    create_account.check_header_title_is('My Account')
    create_account.check_success_registration_alert()
    account_name_value, account_email_value = create_account.get_account_name_and_email()
    assert first_name + ' ' + last_name == account_name_value
    assert email == account_email_value


def test_create_user_with_invalid_data(create_account):
    create_account.open_page(create_account.page_url)
    create_account.check_header_title_is('Create New Customer Account')
    create_account.fill_auth_form()
