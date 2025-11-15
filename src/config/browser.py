from playwright.sync_api import Playwright
def open_browser(playwright:Playwright):
    return playwright.chromium.launch(headless=True)