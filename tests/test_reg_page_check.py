import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reg_page import RegPage


@pytest.fixture(scope="function")
def reg_page(chrome_browser_instance):
    return RegPage(chrome_browser_instance)


def test_reg_page_check_all_fields_text(reg_page):
    reg_page.btn_kc_register.click()

    first_name_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[1]/div/span[2]"
    second_name_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/div/span[2]"
    region_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[2]/div/div/span[2]"
    email_or_phone_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[3]/div/div/span[2]"
    password_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[1]/div/span[2]"
    confirm_password_span_xpath = "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/div/span[2]"

    first_name_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, first_name_span_xpath))
    )
    assert first_name_span.text == "Имя"

    second_name_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, second_name_span_xpath))
    )
    assert second_name_span.text == "Фамилия"

    region_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, region_span_xpath))
    )
    assert region_span.text == "Регион"

    email_or_phone_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, email_or_phone_span_xpath))
    )
    assert email_or_phone_span.text == "E-mail или мобильный телефон"

    password_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, password_span_xpath))
    )
    assert password_span.text == "Пароль"

    confirm_password_span = WebDriverWait(reg_page._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, confirm_password_span_xpath))
    )
    assert confirm_password_span.text == "Подтверждение пароля"


def test_reg_page_register_button_text_color(reg_page):
    reg_page.btn_kc_register.click()
    register_button_text = reg_page.btn_register.get_text()
    assert register_button_text == "Зарегистрироваться"
    register_button = reg_page._web_driver.find_element(By.XPATH, '//button[@name="register"]')
    button_color = register_button.value_of_css_property('background-color')
    expected_color = 'rgba(255, 79, 18, 1)'
    assert button_color == expected_color
