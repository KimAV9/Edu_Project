class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def main_page(self):
        return self.browser.get('https://www.coursera.org/')
