import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        self._page = page
        self.name_input = page.get_by_placeholder("Name")
        self.email_input = page.get_by_placeholder("Email", exact=True)
        self.subject_input = page.get_by_placeholder("Subject")
        self.message_input = page.get_by_placeholder("Your Message Here")
        self.upload_file_input = page.locator("[name='upload_file']")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.success_message = page.locator("//*[contains(@class, 'status')]")
        self.home_btn = page.locator("//*[contains(@class, 'btn-success')]")
        super().__init__(page, page.get_by_role("heading", name="Get In Touch"), "/contact_us")

    def fill_in_information(self, contact_info, file_path):
        self.__confirm_allert()
        self.name_input.type(contact_info.name, delay=50)
        self.email_input.type(contact_info.email, delay=50)
        self.subject_input.type(contact_info.subject, delay=50)
        self.message_input.type(contact_info.message, delay=50)
        self.__upload_file(file_path)
        self.submit_btn.click()

    def __confirm_allert(self):
        self._page.on("dialog", lambda dialog: dialog.accept())

    def __upload_file(self, file_path):
        self.upload_file_input.set_input_files(file_path)
        allure.attach.file(
            file_path,
            name="contact-attach"
        )
