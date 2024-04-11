from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.ID, 'email')
PASSWORD_FIELD = (By.ID, 'pass')
SUBMIT_BUTTON = (By.ID, 'send2')
ERROR_ALERT = (By.XPATH, '//div[@data-ui-id="message-error"]')
ACC_INFO = (By.XPATH, '(//div[@class="box-content"])[1]')
EMAIL_ERROR = (By.XPATH, '//div[@id="email-error"]')
PASSWORD_ERROR = (By.XPATH, '//div[@id="pass-error"]')
