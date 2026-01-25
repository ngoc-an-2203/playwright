import pytest
from typing import Generator
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "username,password,expect_success",
    [
        ("AnTestHB", "123456", True),
        ("ABC", "XYZABBBBB", False),
    ]
)
def test_login_reuse(page: Page, username: str, password: str, expect_success: bool):
    page.set_default_timeout(60000)  # Increase timeout to 60 seconds
    page.goto("https://demo.hanbai.vn/login")
    page.get_by_role("textbox", name="Nhập tên tài khoản").fill(username)
    page.get_by_role("textbox", name="Nhập mật khẩu").fill(password)
    page.get_by_role("button", name="Đăng nhập").click()

    if expect_success:
        page.get_by_text("Tiếp tục đăng nhập", exact=True).click()
        page.get_by_role("button", name="Đăng nhập").click()
        expect(page.locator("a").first).to_be_visible()
    else:
        expect(page.get_by_text("Đăng nhập thất bại. Vui lòng")).to_be_visible()
