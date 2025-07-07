from element.login_element import LoginSelector
from action.basic_action import BasicAction

class LoginUIT:
    def __init__(self, page):
        self.action = BasicAction(page)
        self.sel = LoginSelector
        self.page = page

    def verify_login_failed(self):
        self.page.wait_for_selector(self.sel.error_msg)
        assert "Epic sadface" in self.action.get_text(self.sel.error_msg)

    def verify_login_success(self):
        self.page.wait_for_url("**/inventory.html")
        assert "inventory.html" in self.page.url
