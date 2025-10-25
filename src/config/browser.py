def open_browser(playwright):
    return playwright.chromium.launch(headless=False)