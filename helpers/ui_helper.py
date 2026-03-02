import pickle
import os
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from faker import Faker
from data.creds import Credentials
from metaclasses.meta_locators import MetaLocator


faker = Faker()

class UIHelper(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.fake = Faker()
        self.creds = Credentials()

    def open(self):
        with allure.step(f"Open page: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)
            self.actions.send_keys().send_keys()

    def is_opened(self):
        with allure.step(f"Page {self._PAGE_URL} is opened"):
            self.wait.until(EC.url_contains(self._PAGE_URL))

    def find(self, locator: tuple, wait_off=False) -> WebElement:
        """
        This method helps to find element
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        if wait_off:
            return self.driver.find_element(locator)
        else:
            element = self.wait.until(EC.visibility_of_element_located(locator))
        return element


    def find_all(self, locator: tuple) -> list[WebElement]:
        """
    This method helps to find list of all elements
    :param locator: Not unpacked tuple
    :return: WebElements list
        """
        elements = self.wait_visibility_of_elements(locator)
        return elements

    def click(self, locator: tuple):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def fill(self, locator: tuple, text: str):
        self.find(locator).send_keys(text)


    def is_checked(self, locator):
        self.find(locator).get_attribute("checked")

# --- Allure ---

    def screenshot(self, screenshot_name=f"screen_{faker.time()}"):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    # --- Waits ---

    def wait_for_presents(self, locator: tuple,  message=None):
        return self.wait.until(EC.presence_of_element_located(locator), message=message)


    def wait_for_visibility(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator), message=message)


    def wait_for_invisibility(self, locator: tuple | WebElement, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.invisibility_of_element(locator), message=message)


    def wait_for_clickable(self, locator: tuple, message=None):
        """
            This method waits for visibility
            :param locator: Not unpacked tuple
            :return: WebElement
            """
        return self.wait.until(EC.element_to_be_clickable(locator), message=message)


    def wait_visibility_of_elements(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)

        # --- Cookies ---


    def save_cookies(self, cookies_name="login-cookies"):
        with open(f"cookies/{cookies_name}.pkl", "wb") as cookies_file:
            pickle.dump(self.driver.get_cookies(), cookies_file)


    def load_cookies(self, cookies_name="login-cookies"):
        with open(f"cookies/{cookies_name}.pkl", "rb") as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.refresh()


        # --- Scrolls ---

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")


    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")


    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
            window.scrollTo({
                top: window.scrollY + 500,
            });
            """)