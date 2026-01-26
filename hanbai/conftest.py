import pytest
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page
from config import HANBAI_AUTH_FILE as AUTH_FILE, TIMEOUT, HANBAI_BASE_URL
import slugify
import os
import shutil

@pytest.fixture(scope="session", autouse=True)
def clear_traces(request):
    traces_dir = "traces"
    if os.path.exists(traces_dir):
        shutil.rmtree(traces_dir)
    os.makedirs(traces_dir)

@pytest.fixture
def auth_context(browser: Browser, request) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(
        storage_state=AUTH_FILE,
        base_url=HANBAI_BASE_URL,
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(TIMEOUT)
    context.set_default_navigation_timeout(TIMEOUT)
    yield context
    
    trace_path = f"traces/{slugify.slugify(request.node.name)}.zip"
    context.tracing.stop(path=trace_path)
    context.close()

@pytest.fixture
def auth_page(auth_context: BrowserContext) -> Page:
    page = auth_context.new_page()
    return page
