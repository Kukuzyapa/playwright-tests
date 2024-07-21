import re

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        self._page = page
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_btn = page.locator("button#submit_search")
        self.searched_products_header = page.get_by_role("heading", name="Searched Products")

        super().__init__(page, self.search_input)

    def search_items(self, item):
        self.search_input.fill(item)
        self.search_btn.click()

    def expect_results_contain_item(self, pattern):
        self._page.wait_for_load_state("domcontentloaded")
        for cart in self._page.locator("//*[@class='features_items']/div[not(@id)]").all():
            expect(cart).to_contain_text(re.compile(pattern), ignore_case=True)