# from playwright.sync_api import sync_playwright
# from pages.element import *

# def test_search():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, args=["--start-maximized"])  # 設為 False 會開啟瀏覽器
#         page = browser.new_page(no_viewport=True)
#         page.goto("https://www.youtube.com/")

#         # 輸入搜尋關鍵字
#         page.fill("input[name='search_query']", 'Apink')
#         page.press("input[name='search_query']", 'Enter')
#         # 等待結果載入
#         page.wait_for_selector('ytd-video-renderer')

#         # 截圖保存
#         page.screenshot(path="bing_result.png")

#         browser.close()

# if __name__ == "__main__":
#     test_search()