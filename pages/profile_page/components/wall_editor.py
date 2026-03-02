import time

from helpers.ui_helper import UIHelper
import allure

class WallEditor(UIHelper):

    _SWITCH_CALENDAR_LABEL = "//label[contains(@class, 'switch-input') and preceding-sibling::p[text()='Calendar']]"
    _SWITCH_CALENDAR_INPUT = "//label[contains(@class, 'switch-input') and preceding-sibling::p[text()='Calendar']]/input"
    _SAVE_CHANGES_BUTTON = "//div[@class='centered-block']//button[@title='Save Changes']"

    @allure.step("Turn on wall calendar option")
    def switch_wall_calendar_option(self):
        self.scroll_to_bottom()
        calendar_input = self.wait_for_presents(self._SWITCH_CALENDAR_INPUT)
        self.click(self._SWITCH_CALENDAR_LABEL)
        self.screenshot()
        return calendar_input.is_selected()

    @allure.step("Save changes")
    def save_changes(self):
        try:
            save_button = self.find(self._SAVE_CHANGES_BUTTON)
            if save_button.is_displayed():
                save_button.click()
        except:
            pass