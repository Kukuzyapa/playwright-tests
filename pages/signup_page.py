from playwright.sync_api import Page

from models.signup_user import RegisterUser
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        self._page = page
        self.enter_info_header = page.get_by_role("heading", name="Enter Account Information")
        self.password_field = page.locator("#password")
        self.day_of_birth = page.locator("#days")
        self.month_of_birth = page.locator("#months")
        self.year_of_birth = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.special_offers_checkbox = page.locator("#optin")
        self.first_name_field = page.locator("#first_name")
        self.last_name_field = page.locator("#last_name")
        self.company_field = page.locator("#company")
        self.address1_field = page.locator("#address1")
        self.address2_field = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_field = page.locator("#state")
        self.city_field = page.locator("#city")
        self.zipcode_field = page.locator("#zipcode")
        self.mobile_number_field = page.locator("#mobile_number")
        self.create_account_btn = page.get_by_role("button", name="Create Account")
        self.account_created_header = page.get_by_role("heading", name="Account Created!")
        self.continue_btn = page.get_by_role("link", name="Continue")

        super().__init__(page, self.enter_info_header)

    def fill_in(self, user: RegisterUser):
        self._page.get_by_role("radio", name=user.title).check()
        self.password_field.fill(user.password)
        self.day_of_birth.select_option(user.date_of_birth.day)
        self.month_of_birth.select_option(user.date_of_birth.month)
        self.year_of_birth.select_option(user.date_of_birth.year)
        self.newsletter_checkbox.check() if user.newsletter else None
        self.special_offers_checkbox.check() if user.special_offers else None
        self.first_name_field.fill(user.address.first_name)
        self.last_name_field.fill(user.address.last_name)
        self.company_field.fill(user.address.company)
        self.address1_field.fill(user.address.address)
        self.address2_field.fill(user.address.address2)
        self.country_select.select_option(user.address.country)
        self.state_field.fill(user.address.state)
        self.city_field.fill(user.address.city)
        self.zipcode_field.fill(user.address.zipcode)
        self.mobile_number_field.fill(user.address.mobile_number)
        self.create_account_btn.click()
