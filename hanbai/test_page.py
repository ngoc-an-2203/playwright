import re
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize(
    "path,expect_success",
    [
        ("/menu/a/a/aa010", True),
        ("/menu/a/a/aa020", True),
        ("/menu/a/a/aa030", True),
        ("/menu/a/a/aa040", True),
        ("/menu/a/a/aa050", True),
        ("/menu/a/b/aa050", False),
    ]
)
def test_page(auth_page: Page, path, expect_success):
    auth_page.goto(path)
    if expect_success:
        expect(auth_page.locator(".Section_PageName > img")).to_be_visible()
    else:
        expect(auth_page.locator("div").filter(has_text="QUAY VỀ TRANG ĐĂNG NHẬP").nth(4)).to_be_visible()
