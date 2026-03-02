from helpers.ui_helper import UIHelper
import allure

class MeetingDropdown(UIHelper):

    _BROADCASTER_LINK = "//ul[@role='menu']//a[@title='Broadcaster']"
    _WEB_CONTROLS = "//ul[@role='menu']//a[@title='Web Controls']"
    _MEETING_WALL = "//ul[@role='menu']//a[@title='Go to Meeting Wall']"
    _WALL_EDITOR = "//ul[@role='menu']//a[@title='Go to Wall Editor']"
    _LEARN_MORE = "//ul[@role='menu']//a[@title='Broadcaster']"


    @allure.step("Click broadcoaster")
    def click_broadcoaster(self):
        self.click(self._BROADCASTER_LINK)

    @allure.step("Click web_controls")
    def click_web_controls(self):
        self.click(self._WEB_CONTROLS)

    @allure.step("Click meeting_wall")
    def click_meeting_wall(self):
        self.click(self._MEETING_WALL)

    @allure.step("Click wall_editor")
    def click_wall_editor(self):
        self.click(self._WALL_EDITOR)

    @allure.step("Click learn_more")
    def click_learn_more(self):
        self.click(self._LEARN_MORE)
