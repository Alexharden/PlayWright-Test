class BasicAction:
    def __init__(self, page):
        self.page = page

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def click(self, selector):
        self.page.click(selector)

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()
