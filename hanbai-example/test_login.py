import pytest
from typing import Generator
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def run_around_tests(page: Page) -> Generator[None, None, None]:
    # setup before a test
    page.set_default_timeout(60000)  # Increase timeout to 60 seconds
    page.goto("https://demo.hanbai.vn/login")
    # run the actual test
    yield
    # run any cleanup code

def test_login_success(page: Page) -> None:
    # page.get_by_role("textbox", name="Nhập tên tài khoản").click()
    page.get_by_role("textbox", name="Nhập tên tài khoản").fill("AnTestHB")
    # page.get_by_role("textbox", name="Nhập mật khẩu").click()
    page.get_by_role("textbox", name="Nhập mật khẩu").fill("123456")
    page.get_by_role("button", name="Đăng nhập").click()
    page.get_by_text("Tiếp tục đăng nhập", exact=True).click()
    page.get_by_role("button", name="Đăng nhập").click()
    expect(page.locator("a").first).to_be_visible()

def test_login_failed(page: Page) -> None:
    page.get_by_role("textbox", name="Nhập tên tài khoản").click()
    page.get_by_role("textbox", name="Nhập tên tài khoản").fill("ABC")
    page.get_by_role("textbox", name="Nhập mật khẩu").click()
    page.get_by_role("textbox", name="Nhập mật khẩu").fill("XYZABBBBB")
    page.get_by_role("button", name="Đăng nhập").click()
    expect(page.get_by_text("Đăng nhập thất bại. Vui lòng")).to_be_visible()
