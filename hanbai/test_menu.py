import re
from playwright.sync_api import Page, expect
from config import HANBAI_BASE_URL as BASE_URL

def test_menu_visible(auth_page: Page):
    cookies = auth_page.context.cookies()
    print(cookies)
    auth_page.goto(f"{BASE_URL}/menu")
    expect(auth_page).to_have_url(re.compile(r".*/menu$"))
