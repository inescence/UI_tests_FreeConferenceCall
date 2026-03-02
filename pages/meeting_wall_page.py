from base.base_page import BasePage
from data.links import Links


class MeetingPage(BasePage):

    _PAGE_URL = Links.MEETING_WALL_PAGE

    _CALENDAR = "//div[@data-test-calendar]"

