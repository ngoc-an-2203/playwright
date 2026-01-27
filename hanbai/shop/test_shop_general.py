import re
from typing import Generator
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def run_around_tests(auth_page: Page) -> Generator[None, None, None]:
    # setup before a test
    auth_page.goto("/menu/a/a/aa020")
    # run the actual test
    yield
    # run any cleanup code

def test_shop_general(auth_page: Page):
    expect(auth_page.locator(".Section_PageName > img")).to_be_visible()
