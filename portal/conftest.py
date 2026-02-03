import pytest
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page
from config import PORTAL_AUTH_FILE as AUTH_FILE, TIMEOUT, PORTAL_BASE_URL
import slugify
import os
import shutil

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing test collection and execution.
    """
    # This hook ensures that the code only runs on the master node,
    # not on any of the worker nodes.
    if not hasattr(session.config, "workerinput"):
        traces_dir = "traces"
        if os.path.exists(traces_dir):
            shutil.rmtree(traces_dir)
        os.makedirs(traces_dir)

@pytest.fixture
def portal_context(browser: Browser, request) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(
        storage_state=AUTH_FILE,
        base_url=PORTAL_BASE_URL,
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    context.set_default_timeout(TIMEOUT)
    context.set_default_navigation_timeout(TIMEOUT)
    yield context
    
    trace_path = f"traces/{slugify.slugify(request.node.name)}.zip"
    context.tracing.stop(path=trace_path)
    context.close()

@pytest.fixture
def portal_page(portal_context: BrowserContext) -> Page:
    page = portal_context.new_page()
    return page
