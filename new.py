import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/login/?next=/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("alice")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Create new test").click()
    page.locator("#id_name").click()
    page.locator("#id_name").fill("hello")
    page.get_by_role("textbox", name="Test description").click()
    page.get_by_role("textbox", name="Test description").fill("world")
    page.get_by_role("button", name="Create").click()
    page.get_by_role("link", name="Test Cases").click()
    page.get_by_role("cell", name="hello").click()
    page.locator(".ttRem.deleteBtn.delete_18").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
