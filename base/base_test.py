from pages.login_page import LoginPage
from pages.profile_page.profile_page import ProfilePage
from pages.dashboard_page import DashboardPage
from pages.meeting_wall_page import MeetingPage

class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.meeting_wall_page = MeetingPage(self.driver)