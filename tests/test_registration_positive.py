import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reg_page import RegPage

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')

valid_password_email = os.getenv('valid_password_email')
valid_password_phone = os.getenv('valid_password_phone')


@pytest.fixture(scope="function")
def reg_page(chrome_browser_instance):
    return RegPage(chrome_browser_instance)


def test_successful_registration_by_email(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_first_name.send_keys("Александра")
    reg_page.input_last_name.send_keys("Давыдова")
    reg_page.input_email_or_phone.send_keys(valid_email)
    reg_page.input_password.send_keys(valid_password_email)
    reg_page.input_confirm_password.send_keys(valid_password_email)
    reg_page.btn_register.click()
    time.sleep(1)
    confirm_email_title = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div/h1"))
    )
    assert confirm_email_title.text == "Подтверждение email"


def test_successful_registration_by_phone(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_first_name.send_keys("Александра")
    reg_page.input_last_name.send_keys("Давыдова")
    reg_page.input_email_or_phone.send_keys(valid_phone)
    reg_page.input_password.send_keys(valid_password_phone)
    reg_page.input_confirm_password.send_keys(valid_password_phone)
    reg_page.btn_register.click()
    time.sleep(1)
    confirm_phone_title = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div/h1"))
    )
    assert confirm_phone_title.text == "Подтверждение телефона"
