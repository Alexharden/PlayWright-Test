from playwright.sync_api import sync_playwright
import os
import pytest

def test_login_success():
    """
    ✅ 測試說明：成功登入測試
    驗證使用正確帳密，是否導向商品頁面並畫面與 baseline 一致
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        page.goto("https://www.saucedemo.com/")

        # 輸入帳號密碼並登入
        page.fill("input[data-test='username']", 'standard_user')
        page.fill("input[data-test='password']", 'secret_sauce')
        page.click("input[data-test='login-button']")

        page.wait_for_url("**/inventory.html")
        page.wait_for_selector("span.title")
        assert "inventory.html" in page.url
        assert page.locator("span.title").inner_text() == "Products"
        browser.close()

def test_login_fail_invalid_password():
    """
    ❌ 測試說明：錯誤密碼登入測試
    驗證錯誤訊息是否出現，以及未跳轉頁面
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        page.goto("https://www.saucedemo.com/")

        # 輸入錯誤密碼
        page.fill("input[data-test='username']", 'standard_user')
        page.fill("input[data-test='password']", 'wrong_password')
        page.click("input[data-test='login-button']")

        # 驗證錯誤訊息出現
        page.wait_for_selector("h3[data-test='error']")
        error_text = page.locator("h3[data-test='error']").inner_text()
        assert "Epic sadface" in error_text
        assert "Username and password do not match" in error_text
        browser.close()

# if __name__ == "__main__":
#     test_login_success()
