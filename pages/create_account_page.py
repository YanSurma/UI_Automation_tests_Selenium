import allure

from generator.generator import generated_user
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill authorization form with valid data')
    def fill_auth_form(self):
        # Generate data
        user = next(generated_user())
        # Input data
        first_name_field = self.find_and_send_keys(*loc.FIRST_NAME_FIELD, value=user.first_name)
        last_name_field = self.find_and_send_keys(*loc.LAST_NAME_FIELD, value=user.last_name)
        email_field = self.find_and_send_keys(*loc.EMAIL_FIELD, value=user.email)
        password_field = self.find_and_send_keys(*loc.PASSWORD_FIELD, value=user.password)
        confirm_password_field = self.find_and_send_keys(*loc.CONFIRM_PASSWORD_FIELD, value=user.password)
        create_button = self.find(*loc.CREATE_BUTTON).click()
        return user.first_name, user.last_name, user.email

    @allure.step('Fill authorization form with empy fields')
    def fill_auth_form_with_invalid_data(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find_and_send_keys(*loc.FIRST_NAME_FIELD, value=first_name)
        last_name_field = self.find_and_send_keys(*loc.LAST_NAME_FIELD, value=last_name)
        email_field = self.find_and_send_keys(*loc.EMAIL_FIELD, value=email)
        password_field = self.find_and_send_keys(*loc.PASSWORD_FIELD, value=password)
        confirm_password_field = self.find_and_send_keys(*loc.CONFIRM_PASSWORD_FIELD, value=confirm_password)
        create_button = self.find(*loc.CREATE_BUTTON).click()

    @allure.step('Set account name and email')
    def get_account_name_and_email(self):
        account_info = self.find(*loc.ACC_INFO)
        account_name_value = account_info.text.split(sep='\n')[0]
        account_email_value = account_info.text.split(sep='\n')[1]
        return account_name_value, account_email_value

    @allure.step('Check for success alert')
    def check_success_alert(self):
        success_alert = self.find(*loc.SUCCESS_ALERT)
        assert success_alert.text == "Thank you for registering with Main Website Store."

    @allure.step('Check for field error alert')
    def check_error_auth_alert(self):
        error_alert = self.find_all(*loc.ERROR_ALERT)
        assert 'This is a required field.' or 'Please enter the same value again.' in error_alert.text

    @allure.step('Check for password error alert')
    def check_error_password_alert(self):
        error_password_alert = self.find(*loc.ERROR_PASSWORD_ALERT)
        assert error_password_alert.text == 'Please enter the same value again.'
