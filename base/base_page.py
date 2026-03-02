from helpers.ui_helper import UIHelper
from base.base_components.meeting_dropdown import MeetingDropdown
from base.base_components.profile_dropdown import ProfileDropdown

class BasePage(UIHelper):

    @property
    def header(self):
        return Header(self.driver)

class Header(UIHelper):

    _MEETING_DROPDOWN = "//a[text()='Online Meetings']"
    _PROFILE_DROPDOWN = "//li[contains(@class, 'my-profile dropdown')]" #//div[@class='my-name'][1]

    @property
    def meeting_dropdown(self):
        self.click(self._MEETING_DROPDOWN)
        self._menu = MeetingDropdown(self.driver)
        return self._menu

    @property
    def profile_dropdown(self):
        self.click(self._PROFILE_DROPDOWN)
        self._menu = ProfileDropdown(self.driver)
        return self._menu
