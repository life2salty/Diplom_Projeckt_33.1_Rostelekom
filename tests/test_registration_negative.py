import pytest
import os

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


def test_unsuccessful_registration_by_email_already_exists(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_first_name.send_keys("Александра")
    reg_page.input_last_name.send_keys("Давыдова")
    reg_page.input_email_or_phone.send_keys(valid_email)
    reg_page.input_password.send_keys(valid_password_email)
    reg_page.input_confirm_password.send_keys(valid_password_email)
    reg_page.btn_register.click()
    alert_title = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div/div/h2"))
    )
    assert alert_title.text == "Учётная запись уже существует"


def test_unsuccessful_registration_by_phone_already_exists(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_first_name.send_keys("Александра")
    reg_page.input_last_name.send_keys("Давыдова")
    reg_page.input_email_or_phone.send_keys(valid_phone)
    reg_page.input_password.send_keys(valid_password_phone)
    reg_page.input_confirm_password.send_keys(valid_password_phone)
    reg_page.btn_register.click()
    alert_title = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div/div/h2"))
    )
    assert alert_title.text == "Учётная запись уже существует"


def test_validation_registration(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_first_name.send_keys("С")
    reg_page.input_last_name.send_keys("Ф")
    reg_page.input_email_or_phone.send_keys("invalidemail.ru")
    reg_page.input_password.send_keys("qwerty")
    reg_page.input_confirm_password.send_keys("qwerty")
    reg_page.btn_register.click()

    input_error_first_name = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[1]/span"))
    )
    assert input_error_first_name.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    input_error_second_name = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/span"))
    )
    assert input_error_second_name.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    input_error_email_or_phone = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[3]/div/span"))
    )
    assert input_error_email_or_phone.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    input_error_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))
    )
    assert input_error_password.text == "Длина пароля должна быть не менее 8 символов"

    input_error_confirm_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/span"))
    )
    assert input_error_confirm_password.text == "Длина пароля должна быть не менее 8 символов"


def test_validation_registration_password_lowercase_letters(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_password.send_keys("qwerty123")
    reg_page.input_confirm_password.send_keys("qwerty123")
    reg_page.btn_register.click()

    input_error_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))
    )
    assert input_error_password.text == "Пароль должен содержать хотя бы одну заглавную букву"

    input_error_confirm_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/span"))
    )
    assert input_error_confirm_password.text == "Пароль должен содержать хотя бы одну заглавную букву"


def test_validation_registration_password_capital_letters(reg_page):
    reg_page.btn_kc_register.click()
    reg_page.input_password.send_keys("QWERTY123")
    reg_page.input_confirm_password.send_keys("QWERTY123")
    reg_page.btn_register.click()

    input_error_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/span"))
    )
    assert input_error_password.text == "Пароль должен содержать хотя бы одну строчную букву"

    input_error_confirm_password = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/span"))
    )
    assert input_error_confirm_password.text == "Пароль должен содержать хотя бы одну строчную букву"
