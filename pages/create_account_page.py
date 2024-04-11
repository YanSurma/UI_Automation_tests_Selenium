from generator.generator import generated_user
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_auth_form(self):
        # Generate data
        user_info = next(generated_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        password = user_info.password
        confirm_password = user_info.password
        # Input data
        first_name_field = self.find(*loc.FIRST_NAME_FIELD).send_keys(first_name)
        last_name_field = self.find(*loc.LAST_NAME_FIELD).send_keys(last_name)
        email_field = self.find(*loc.EMAIL_FIELD).send_keys(email)
        password_field = self.find(*loc.PASSWORD_FIELD).send_keys(password)
        confirm_password_field = self.find(*loc.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
        create_button = self.find(*loc.CREATE_BUTTON).click()
        return first_name, last_name, email

    def fill_auth_form_with_invalid_data(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find(*loc.FIRST_NAME_FIELD).send_keys(first_name)
        last_name_field = self.find(*loc.LAST_NAME_FIELD).send_keys(last_name)
        email_field = self.find(*loc.EMAIL_FIELD).send_keys(email)
        password_field = self.find(*loc.PASSWORD_FIELD).send_keys(password)
        confirm_password_field = self.find(*loc.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
        create_button = self.find(*loc.CREATE_BUTTON).click()

    def get_account_name_and_email(self):
        account_info = self.find(*loc.ACC_INFO)
        account_name_value = account_info.text.split(sep='\n')[0]
        account_email_value = account_info.text.split(sep='\n')[1]
        return account_name_value, account_email_value

    def check_success_alert(self):
        success_alert = self.find(*loc.SUCCESS_ALERT)
        assert success_alert.text == "Thank you for registering with Main Website Store."

    def check_error_auth_alert(self):
        error_alert = self.find_all(*loc.ERROR_ALERT)
        assert 'This is a required field.' or 'Please enter the same value again.' in error_alert.text

    def check_error_password_alert(self):
        error_password_alert = self.find(*loc.ERROR_PASSWORD_ALERT)
        assert error_password_alert.text == 'Please enter the same value again.'
