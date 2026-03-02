from helpers.ui_helper import UIHelper
import allure


class ProfileDropdown(UIHelper):

    _PROFILE_SETTINGS = "//a[contains(@class, 'profile-settings-link')][1]" #(//a[@title='My profile settings'])[1]

    @allure.step("Click profile settings")
    def click_profile_settings(self):
        self.click(self._PROFILE_SETTINGS)
