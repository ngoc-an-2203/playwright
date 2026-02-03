from playwright.sync_api import Page, expect
from config import PORTAL_AUTH_FILE, PORTAL_BASE_URL as BASE_URL, TIMEOUT, PORTAL_USERNAME, PORTAL_PASSWORD

def test_portal_auth_setup(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto(f"{BASE_URL}/Admin/Auth/Login")
    page.get_by_role("textbox", name="Tên đăng nhập").fill(PORTAL_USERNAME)
    page.get_by_role("textbox", name="Mật khẩu").fill(PORTAL_PASSWORD)
    page.get_by_role("button", name="Đăng nhập").click()
    
    expect(page.get_by_role("link", name=" Dashboard")).to_be_visible()
     # ✅ SAVE AUTH STATE
    # WAIT until the keys you saw in DevTools exist
    page.context.storage_state(path=PORTAL_AUTH_FILE)