from selenium.webdriver.common.by import By

FIRST_NAME_FIELD = (By.ID, "firstname")
LAST_NAME_FIELD = (By.ID, "lastname")
EMAIL_FIELD = (By.ID, "email_address")
PASSWORD_FIELD = (By.ID, "password")
CONFIRM_PASSWORD_FIELD = (By.ID, "password-confirmation")
CREATE_BUTTON = (By.XPATH, '//button[@title="Create an Account"]')
ACC_INFO = (By.XPATH, '(//div[@class="box-content"])[1]')
SUCCESS_ALERT = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
