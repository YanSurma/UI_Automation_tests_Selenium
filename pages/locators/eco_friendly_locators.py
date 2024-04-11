from selenium.webdriver.common.by import By

SELECT_DROP_DOWN = (By.XPATH, '(//select[@id="sorter"])[1]')
ITEM_BANNER = (By.XPATH, '(//div[@class="product-item-info"])[1]')
ADD_BUTTON = (By.XPATH, '(//button[@title="Add to Cart"])[1]')
ADD_LINK = (By.XPATH, '(//a[@class="product-item-link"])[1]')
COMPARE_BUTTON = (By.XPATH, '(//a[@title="Add to Compare"])[1]')
ITEM_NAME = (By.XPATH, '(//a[@class="product-item-link"])[1]')
COMPARE_ALERT = (By.XPATH, '//div[@data-ui-id="message-success"]')
ITEM_PAGE_NAME = (By.XPATH, '//span[@class="base"]')

