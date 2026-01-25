import pytest
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page
from config import HANBAI_AUTH_FILE as AUTH_FILE

@pytest.fixture
def auth_context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(storage_state=AUTH_FILE)
    yield context
    context.close()

@pytest.fixture
def auth_page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    return page
