from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page, locator: Locator, url="/"):
        self._page = page
        self.locator = locator
        self.url = url

    def expect_to_be_displayed(self):
        self.locator.is_visible()
        expect(self.locator).to_be_visible()

    def navigate(self):
        self._page.goto(self.url, wait_until="domcontentloaded")