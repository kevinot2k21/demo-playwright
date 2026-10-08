import pytest
import datetime
from playwright.sync_api import sync_playwright, Page, expect

#Verify Negative Scenario
def test_required_fields(page:Page):
    page.goto("https://www.saucedemo.com/")
    #Enter only Username
    page.locator("#user-name").fill("test user")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("Epic sadface: Password is required")).to_be_visible()

    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    page.screenshot(path=f"screenshots/login/usernameOnly_{timestamp}.png", full_page=True)
    
    #Enter only Password
    page.locator('[data-test="username"]').clear()
    page.locator('[data-test="password"]').fill("pass")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    page.screenshot(path=f"screenshots/login/passwordOnly_{timestamp}.png", full_page=True)

#Verify invalid
def test_invalid_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="password"]').clear()
    page.locator('[data-test="username"]').fill("test user")
    page.locator('[data-test="password"]').fill("pass")
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    page.screenshot(path=f"screenshots/login/invalidCreds_{timestamp}.png", full_page=True)
    
#Verify successful Login
def test_valid_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.wait_for_timeout(2000)
    page.locator("#login-button").click()
    page.wait_for_timeout(2000)

    assert page.url.endswith("/inventory.html")
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    page.screenshot(path=f"screenshots/login/successfulLogin_{timestamp}.png", full_page=True)
