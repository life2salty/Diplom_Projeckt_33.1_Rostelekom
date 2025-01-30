from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.support.ui import Select

class RegPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?'
               'client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&'
               'response_type=code&scope=openid&state=d012f376-66d0-4417-ae7b-c3e4fcbbce9f&'
               'theme&auth_type')
        super().__init__(web_driver, url)

    input_first_name = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    input_last_name = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    input_email_or_phone = WebElement(xpath='//*[@id="address"]')
    input_password = WebElement(xpath='//*[@id="password"]')
    input_confirm_password = WebElement(xpath='//*[@id="password-confirm"]')

    btn_kc_register = WebElement(xpath='//*[@id="kc-register"]')
    btn_register = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/button')

    region_selector = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input')
