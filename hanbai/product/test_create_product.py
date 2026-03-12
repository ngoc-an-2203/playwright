import re
from typing import Generator
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(autouse=True)
def run_around_tests(auth_page: Page) -> Generator[None, None, None]:
    # setup before a test
    auth_page.goto("/menu/b/a/ba010")
    # run the actual test
    yield
    # run any cleanup code

def test_create_product(auth_page: Page):
    auth_page.get_by_role("button", name="Thêm mới").click()
    auth_page.locator("#txt-CShhnNm-ba011").fill("hoa giay 5")
    auth_page.get_by_text("Giá", exact=True).click()
    auth_page.locator("#txt-MHjyjnKouriTnk-ba011").fill("20,0000")
    auth_page.get_by_role("textbox").nth(4).click()
    auth_page.get_by_role("textbox").nth(4).fill("30")
    auth_page.get_by_role("cell", name="30", exact=True).get_by_role("textbox").fill("30,0000")
    auth_page.wait_for_timeout(6000)
    auth_page.get_by_text("Tồn kho").click()
    auth_page.locator("#txt-MZaikoKrkshSu-ba011").click()
    auth_page.locator("#txt-MZaikoKrkshSu-ba011").fill("100")
    auth_page.get_by_role("button", name="Lưu và đóng").click()
    auth_page.locator("#txtProductName").click()
    auth_page.locator("#txtProductName").fill("hoa giay 5")
    auth_page.get_by_role("button", name="Hiển thị").click()
    expect(auth_page.get_by_role("cell", name="hoa giay 5")).to_be_visible()