from playwright.sync_api import Page, expect

AUTH_FILE = "auth.json"
LOGIN_URL = "https://demo.hanbai.vn/login"

def test_auth_setup(page: Page):
    page.set_default_timeout(60000)  # Increase timeout to 60 seconds
    page.goto(LOGIN_URL)

    # 🔽 GENERATED CODE (KEEP AS-IS)
    page.get_by_role("textbox", name="Nhập tên tài khoản").fill("AnTestHB")
    page.get_by_role("textbox", name="Nhập mật khẩu").fill("123456")
    page.get_by_role("button", name="Đăng nhập").click()

    page.get_by_text("Tiếp tục đăng nhập", exact=True).click()
    page.get_by_role("button", name="Đăng nhập").click()

    expect(page.locator("a").first).to_be_visible()

    # ✅ SAVE AUTH STATE
    page.context.storage_state(path=AUTH_FILE)
