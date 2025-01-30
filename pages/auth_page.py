from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?'
               'client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&'
               'response_type=code&scope=openid&state=d012f376-66d0-4417-ae7b-c3e4fcbbce9f&'
               'theme&auth_type')
        super().__init__(web_driver, url)

    btn_tab_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    btn_tab_email = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    btn_tab_login = WebElement(xpath='//*[@id="t-btn-tab-login"]')
    btn_tab_ls = WebElement(xpath='//*[@id="t-btn-tab-ls"]')
    input_username = WebElement(xpath='//*[@id="username"]')
    input_password = WebElement(xpath='//*[@id="password"]')
    forgot_password = WebElement(xpath='//*[@id="forgot_password"]')
    btn_enter = WebElement(xpath='//*[@id="kc-login"]')
    help_modal = WebElement(xpath='//*[@id="faq-open"]/a')
    btn_register = WebElement(xpath='//*[@id="kc-register"]')
