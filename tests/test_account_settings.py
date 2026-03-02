import allure
import pytest
from base.base_test import BaseTest


@allure.epic("Profile")
@allure.feature("Settings")
class TestAccountSettings(BaseTest):

    @pytest.mark.parametrize("run", range(2))
    def test_turn_on_calendar_on_the_wall(self, run):
        self.login_page.open()
        self.login_page.login()
        self.dashboard_page.is_opened()
        self.dashboard_page.header.profile_dropdown.click_profile_settings()
        self.profile_page.is_opened()
        self.profile_page.click_wall_editor_tab()
        self.profile_page.wall_editor.switch_wall_calendar_option()
        self.profile_page.wall_editor.save_changes()
        self.profile_page.is_changes_saved()
        self.profile_page.header.meeting_dropdown.click_meeting_wall()
        self.meeting_wall_page.is_opened()