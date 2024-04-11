import pytest
from selenium import webdriver
from time import sleep

from pages.create_account import CreateAccount
from pages.customer_login_page import CustomerLogin
from pages.whats_new_page import WhatsNew


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    sleep(2)


@pytest.fixture()
def whats_new(driver):
    return WhatsNew(driver)


@pytest.fixture()
def customer_login(driver):
    return CustomerLogin(driver)


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)
