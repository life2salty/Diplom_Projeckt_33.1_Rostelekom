import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')

valid_password_email = os.getenv('valid_password_email')
valid_password_phone = os.getenv('valid_password_phone')


@pytest.fixture(scope="function")
def auth_page(chrome_browser_instance):
    return AuthPage(chrome_browser_instance)


def test_successful_auth_by_email(auth_page):
    auth_page.btn_tab_email.click()
    auth_page.input_username.send_keys(valid_email)
    auth_page.input_password.send_keys(valid_password_email)
    auth_page.btn_enter.click()
    time.sleep(1)  # если требуется ввести капчу
    heading = WebDriverWait(auth_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    )
    last_name_span = heading.find_element(By.XPATH, "./span[1]")
    first_name_span = heading.find_element(By.XPATH, "./span[2]")
    assert last_name_span.text == "Давыдова"
    assert first_name_span.text == "Александра"
    time.sleep(1)

def test_successful_auth_by_phone(auth_page):
    auth_page.input_username.send_keys(valid_phone)
    auth_page.input_password.send_keys(valid_password_phone)
    auth_page.btn_enter.click()
    time.sleep(1)  # если требуется ввести капчу
    heading = WebDriverWait(auth_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    )
    last_name_span = heading.find_element(By.XPATH, "./span[1]")
    first_name_span = heading.find_element(By.XPATH, "./span[2]")
    assert last_name_span.text == "Давыдова"
    assert first_name_span.text == "Александра"
    time.sleep(1)

def test_successful_auth_by_login(auth_page):
    auth_page.btn_tab_login.click()  # можно не переключаться между табами и вводить логин во вкладке "Телефон"
    auth_page.input_username.send_keys(valid_login)
    auth_page.input_password.send_keys(valid_password_email)
    auth_page.btn_enter.click()
    time.sleep(1)  # если требуется ввести капчу
    heading = WebDriverWait(auth_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    )
    last_name_span = heading.find_element(By.XPATH, "./span[1]")
    first_name_span = heading.find_element(By.XPATH, "./span[2]")
    assert last_name_span.text == "Давыдова"
    assert first_name_span.text == "Александра"
