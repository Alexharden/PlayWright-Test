from element.login_element import LoginSelector
from action.basic_action import BasicAction

class LoginFlow:
    def __init__(self, page, test_data):
        self.action = BasicAction(page)
        self.sel = LoginSelector
        self.url = test_data["url"]
        self.page = page

    def login(self, username, password):
        self.page.goto(self.url)
        self.action.fill(self.sel.username_input, username)
        self.action.fill(self.sel.password_input, password)
        self.action.click(self.sel.login_button)
