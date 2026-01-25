from playwright.sync_api import Page, expect
from config import HANBAI_AUTH_FILE as AUTH_FILE, HANBAI_BASE_URL as BASE_URL, TIMEOUT

def test_hanbai_auth_setup(page: Page):
    page.set_default_timeout(TIMEOUT)
    page.goto(f"{BASE_URL}/login")

    # 🔽 GENERATED CODE (KEEP AS-IS)
    page.get_by_role("textbox", name="Nhập tên tài khoản").fill("AnTestHB")
    page.get_by_role("textbox", name="Nhập mật khẩu").fill("123456")
    page.get_by_role("button", name="Đăng nhập").click()

    page.get_by_text("Tiếp tục đăng nhập", exact=True).click()
    page.get_by_role("button", name="Đăng nhập").click()

    expect(page.locator("a").first).to_be_visible()

    # ✅ SAVE AUTH STATE
    # WAIT until the keys you saw in DevTools exist
    page.wait_for_function("""
    () => 
    localStorage.getItem('session_user_login') !== null &&
    localStorage.getItem('session_save_userid') !== null &&
    localStorage.getItem('session_page_stack') !== null &&
    localStorage.getItem('dataCompany') !== null &&
    localStorage.getItem('branch') !== null
    """)
    page.context.storage_state(path=AUTH_FILE)