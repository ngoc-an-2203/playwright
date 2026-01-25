import pytest
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page
from config import HANBAI_AUTH_FILE as AUTH_FILE, TIMEOUT, HANBAI_BASE_URL

@pytest.fixture
def auth_context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(
        storage_state=AUTH_FILE,
        base_url=HANBAI_BASE_URL,
    )
    context.set_default_timeout(TIMEOUT)
    context.set_default_navigation_timeout(TIMEOUT)
    yield context
    context.close()

@pytest.fixture
def auth_page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    return page
