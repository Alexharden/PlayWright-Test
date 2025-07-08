from element.login_element import LoginSelector
from action.basic_action import BasicAction

class LoginUIT:
    def __init__(self, page):
        self.action = BasicAction(page)
        self.sel = LoginSelector
        self.page = page
    def verify_login_failed(self):
        self.page.wait_for_selector(self.sel.error_msg)
        error_text = self.action.get_text(self.sel.error_msg)
        assert "Epic sadface" in error_text, "❌ 未出現預期錯誤訊息"
        assert "Username and password do not match" in error_text, "❌ 錯誤訊息內容不符"

    def verify_login_success(self):
        self.page.wait_for_url("**/inventory.html", timeout=5000)
        assert "inventory.html" in self.page.url, "❌ 未導向至商品頁面"

    # def verify_login_failed(self):
    #     try:
    #         self.page.wait_for_selector(self.sel.error_msg)
    #         error_text = self.action.get_text(self.sel.error_msg)
    #         # self.action.take_screenshot("login_failed_check")  # ✅ 每次都先截圖
    #         assert "Epic sadface" in error_text
    #     except AssertionError as e:
    #         self.action.take_screenshot("login_error_text_incorrect")
    #         # 後續 screenshot 錯誤再放這
    #         raise e

    # def verify_login_success(self):
    #     try:
    #         self.page.wait_for_url("**/inventory.html")
    #         # self.action.take_screenshot("login_success_check")  # ✅ 每次都先截圖
    #         assert "inventory.html" in self.page.url
    #     except AssertionError as e:
    #         self.action.take_screenshot("login_success_fail")
    #         # 後續 screenshot 錯誤再放這
    #         raise e
