import json
from playwright.sync_api import sync_playwright
from flows.login_flow import LoginFlow
from uit.login_uit import LoginUIT

def load_test_data():
    with open("test_data.json", encoding="utf-8") as f:
        return json.load(f)

def test_login_success():
    test_data = load_test_data()
    user = test_data["valid_user"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        LoginFlow(page, test_data).login(user["username"], user["password"])
        LoginUIT(page).verify_login_success()
        browser.close()

def test_login_fail_invalid_password():
    test_data = load_test_data()
    user = test_data["invalid_user"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        LoginFlow(page, test_data).login(user["username"], user["password"])
        LoginUIT(page).verify_login_failed()

        browser.close()

