from time import sleep
from pages.base_page import BasePage
from pages.locators import customer_login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'
    user_email = 'yansurma@gmail.com'
    user_password = 'Qna89Vw.HEVSH2F'
    user_name = 'Yan Surma'

    def fill_login_form(self, email, password):
        email_field = self.find(*loc.EMAIL_FIELD)
        pass_field = self.find(*loc.PASSWORD_FIELD)
        submit_button = self.find(*loc.SUBMIT_BUTTON)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        submit_button.click()

    def check_auth_account_data(self, name, email):
        acc_info = self.find(*loc.ACC_INFO)
        acc_name = acc_info.text.split(sep='\n')[0]
        acc_email = acc_info.text.split(sep='\n')[1]
        assert acc_name == name
        assert acc_email == email

    def check_error_alert_text_is(self):
        error_message = self.find(*loc.ERROR_ALERT)
        sleep(2)
        assert error_message.text == 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
