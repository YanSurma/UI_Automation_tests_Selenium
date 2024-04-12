import allure
import pytest
from data.invalid_data import invalid_auth_data, not_equal_passw


@allure.feature('Positive run')
def test_create_user(create_account):
    create_account.open_page(create_account.page_url)
    create_account.check_header_title_is('Create New Customer Account')
    first_name, last_name, email = create_account.fill_auth_form()
    create_account.check_header_title_is('My Account')
    create_account.check_success_alert()
    account_name_value, account_email_value = create_account.get_account_name_and_email()
    assert first_name + ' ' + last_name == account_name_value
    assert email == account_email_value


@allure.feature('Negative run')
@pytest.mark.parametrize('data', invalid_auth_data)
def test_create_user_with_empty_fields(create_account, data):
    create_account.open_page(create_account.page_url)
    create_account.check_header_title_is('Create New Customer Account')
    create_account.fill_auth_form_with_invalid_data(*data)
    create_account.check_error_auth_alert()


@allure.feature('Negative run')
def test_create_user_with_not_equal_passwords(create_account):
    create_account.open_page(create_account.page_url)
    create_account.check_header_title_is('Create New Customer Account')
    create_account.fill_auth_form_with_invalid_data(*not_equal_passw)
    create_account.check_error_password_alert()
