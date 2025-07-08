import os
from playwright.sync_api import TimeoutError
from datetime import datetime


class BasicAction:
    def __init__(self, page, timeout=5000):  # timeout 單位是毫秒
        self.page = page
        self.timeout = timeout

    def wait(self, selector):
        try:
            self.page.wait_for_selector(selector, timeout=self.timeout)
        except TimeoutError:
            self.take_screenshot(f"wait_timeout_{self._safe_name(selector)}")
            raise AssertionError(f"❌ 元素等待逾時：{selector}")

    def click(self, selector):
        self.wait(selector)
        self.page.click(selector)

    def fill(self, selector, value):
        self.wait(selector)
        self.page.fill(selector, value)

    def get_text(self, selector):
        self.wait(selector)
        return self.page.locator(selector).inner_text()

    def take_screenshot(self, filename: str):
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_filename = f"{filename}_{timestamp}.png"
        path = os.path.join("screenshots", full_filename)
        self.page.screenshot(path=path)
        print(f"🖼 已儲存錯誤畫面：{path}")

    def _safe_name(self, raw_selector: str) -> str:
        # 將 selector 轉為適合檔名的格式
        return raw_selector.replace("[", "_").replace("]", "_").replace("=", "-").replace("'", "")


# class BasicAction:
#     def __init__(self, page):
#         self.page = page

#     def fill(self, selector, text):
#         self.page.fill(selector, text)

#     def click(self, selector):
#         self.page.click(selector)

#     def get_text(self, selector):
#         return self.page.locator(selector).inner_text()
    
#     def take_screenshot(self, name: str = "screenshot", folder: str = "screenshots"):
#         os.makedirs(folder, exist_ok=True)
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         path = os.path.join(folder, f"{name}_{timestamp}.png")
#         self.page.screenshot(path=path)
#         print(f"📸 截圖已儲存：{path}")
    

