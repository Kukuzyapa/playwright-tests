import allure
import pytest
from playwright.sync_api import Page, expect

from config.config_manager import ConfigManager
from models.contact_info import ContactInfo
from models.signup_user import RegisterUser
from pages.contact_us_page import ContactUsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.signup_page import SignupPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


class TestDemo:

    @allure.title("Test Register")
    def test_register(self, page: Page):
        user = RegisterUser(**ConfigManager.read_json_data("account_info.json"))
        main_page = MainPage(page)
        login_page = LoginPage(page)
        signup_page = SignupPage(page)

        with allure.step("Step 1. Navigate"):
            main_page.navigate()
            main_page.expect_to_be_displayed()

        with allure.step("Step 2. Click Login"):
            main_page.click_login_btn()
            expect(login_page.new_user_header).to_be_visible()

        with allure.step("Step 3. Register User"):
            login_page.signup(user)
            signup_page.expect_to_be_displayed()

        with allure.step("Step 4. Fill In Information"):
            signup_page.fill_in(user)
            signup_page.continue_btn.click()
            expect(main_page.logged_in_as_header).to_contain_text(user.name)

        with allure.step("Step 5. Delete account"):
            main_page.delete_account_btn.click()
            expect(main_page.account_deleted_header).to_be_visible()
            main_page.continue_btn.click()

    @allure.title("Test Contact Us")
    def test_contact_us_form(self, page: Page):
        main_page = MainPage(page)
        contact_us_page = ContactUsPage(page)
        contact_info = ContactInfo(**ConfigManager.read_json_data("contact_info.json"))
        file_path = ConfigManager.get_artifact_path("cat.png")

        with allure.step("Step 1. Navigate"):
            main_page.navigate()
            main_page.expect_to_be_displayed()

        with allure.step("Step 2. Click contact us"):
            main_page.contact_us_btn.click()
            contact_us_page.expect_to_be_displayed()

        with allure.step("Step 3. Fill in information"):
            contact_us_page.fill_in_information(contact_info, file_path)
            contact_us_page.home_btn.click()
            main_page.expect_to_be_displayed()

    @allure.title("Test Search Product")
    def test_search_product(self, page: Page):
        main_page = MainPage(page)
        product_page = ProductPage(page)
        product_name = "tshirt"
        re_pattern = "t[- ]?shirt"

        with allure.step("Step 1. Navigate"):
            main_page.navigate()
            main_page.expect_to_be_displayed()

        with allure.step("Step 2. Click products"):
            main_page.products_btn.click()
            product_page.expect_to_be_displayed()

        with allure.step("Step 3. Search product"):
            product_page.search_items(product_name)
            expect(product_page.searched_products_header).to_be_visible()
            product_page.expect_results_contain_item(re_pattern)
