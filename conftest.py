import pytest
from selenium import webdriver
from time import sleep

from pages.create_account_page import CreateAccount
from pages.customer_login_page import CustomerLogin
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    sleep(2)


@pytest.fixture()
def customer_login(driver):
    return CustomerLogin(driver)


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
