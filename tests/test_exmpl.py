import re

from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # expect(page).to_have_title(re.compile("Playwright"))
    assert "Playwright" in page.title()


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_example(page: Page):
    page.goto("https://example.com")

    assert "Example Domain" in page.title()

    page.get_by_role("link", name="Learn more").click()

    page.wait_for_load_state("load")
    assert "iana.org" in page.url
