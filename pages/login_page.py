import os
import allure
from data.links import Links
from base.base_page import BasePage

class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _LOGIN_FIELD = "//input[@id='login_email']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _GDPR_CHECKBOX = "(//input[@type='checkbox'])[1]"
    _SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

    @allure.step("Login in account")
    def login(self):
        if os.path.exists("cookies/login-cookies.pkl"):
            self.driver.delete_all_cookies()
            self.load_cookies("login-cookies")
        else:
            self.fill(self._LOGIN_FIELD, self.creds.LOGIN)
            self.fill(self._PASSWORD_FIELD, self.creds.PASSWORD)
            self.click(self._GDPR_CHECKBOX)
            self.click(self._SUBMIT_BUTTON)
            self.save_cookies("login-cookies")







