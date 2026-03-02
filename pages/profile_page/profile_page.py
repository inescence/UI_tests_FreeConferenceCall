import time

from base.base_page import BasePage
from pages.profile_page.components.wall_editor import WallEditor
from data.links import Links
import allure

class ProfilePage(BasePage):

    _PAGE_URL = Links.PROFILE_SETTINGS_PAGE

    _USER_INFO_TAB = "//a[text()='User Information']"
    _UPGRADES_TAB = "//a[text()='Upgrages']"
    _MEETING_TAB = "//a[text()='Meeting']"
    _SECURITY_TAB = "//a[text()='Security']"
    _EMAIL_TAB = "//a[text()='Email']"
    _WALL_EDITOR_TAB = "//a[text()='Wall Editor']"
    _INTEGRATION_TAB = "//a[text()='Integrations']"
    _PAYMENT_INFO_TAB = "//a[text()='Payment Info']"

    _SUCCESS_FLASH = "//div[@class='ftext']"


    @allure.step("Click wall editor tab")
    def click_wall_editor_tab(self):
        self.click(self._WALL_EDITOR_TAB)

    @allure.step("Changes saved")
    def is_changes_saved(self):
        flash = self.wait_for_visibility(self._SUCCESS_FLASH)
        assert flash.text == "Information has been saved.", "Changes wasn't saved"
        self.wait_for_invisibility(flash)



    @property
    def wall_editor(self):
        return WallEditor(self.driver)

