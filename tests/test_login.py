import json
from playwright.sync_api import sync_playwright
from flows.login_flow import LoginFlow
from uit.login_uit import LoginUIT


def load_test_data(evn="production"):
    with open("test_data.json", encoding="utf-8") as f:
        all_data = json.load(f)
        return all_data[evn]
def test_login_success():
    test_data = load_test_data()
    user = test_data["valid_user"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        flow = LoginFlow(page, test_data)
        uit = LoginUIT(page)

        try:
            flow.login(user["username"], user["password"])
            uit.verify_login_success()
        except Exception as e:
            flow.screen_shot("login_success_fail")
            raise e
        finally:
            browser.close()

def test_login_fail_invalid_password():
    test_data = load_test_data()
    user = test_data["invalid_user"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        flow = LoginFlow(page, test_data)
        uit = LoginUIT(page)

        try:
            flow.login(user["username"], user["password"])
            uit.verify_login_failed()
        except Exception as e:
            flow.screen_shot("login_invalid_password_fail")
            raise e
        finally:
            browser.close()

# def test_login_success():
#     test_data = load_test_data()
#     user = test_data["valid_user"]

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         LoginFlow(page, test_data).login(user["username"], user["password"])
#         LoginUIT(page).verify_login_success()
#         browser.close()

# def test_login_fail_invalid_password():
#     test_data = load_test_data()
#     user = test_data["invalid_user"]

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         LoginFlow(page, test_data).login(user["username"], user["password"])
#         LoginUIT(page).verify_login_failed()

#         browser.close()

