import re

from playwright.sync_api import Page
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        self._page = page
        self.login_btn = page.locator("//*[contains(text(), 'Login')]")  # TODO Header
        self.contact_us_btn = page.locator("//*[contains(text(), 'Contact us')]")
        self.logged_in_as_header = page.get_by_text(re.compile("Logged in as"))
        self.delete_account_btn = page.get_by_role("link", name=re.compile("Delete Account"))
        self.account_deleted_header = page.get_by_role("heading", name="Account Deleted!")
        self.continue_btn = page.get_by_role("link", name="Continue")
        self.products_btn = page.locator("//*[contains(text(), 'Products')]")

        super().__init__(page, page.get_by_role("button", name="Test Cases"))

    def click_login_btn(self):
        self.login_btn.click()
