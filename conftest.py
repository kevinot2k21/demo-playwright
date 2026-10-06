import pytest
import pytest_html
from playwright.sync_api import Page


@pytest.fixture
def sauce_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extras = getattr(report, "extras", [])

        if report.failed:
            page = item.funcargs.get("page")

            if page:
                screenshot = page.screenshot(full_page=True)

                extras.append(
                    pytest_html.extras.image(
                        screenshot,
                        mime_type="image/png",
                        name="Failure Screenshot"
                    )
                )

        report.extras = extras