from playwright.sync_api import Page

from models.signup_user import RegisterUser
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        self._page = page
        self.new_user_header = page.get_by_role("heading", name="New User Signup!")
        self.name = page.get_by_placeholder("Name")
        self.email = page.locator("//*[@data-qa='signup-email']")
        self.signup_btn = page.get_by_role("button", name="Signup")
        super().__init__(page, page.get_by_role("button", name="Login"), "/login")

    def signup(self, user: RegisterUser):
        self.name.fill(user.name)
        self.email.fill(user.email)
        self.signup_btn.click()
