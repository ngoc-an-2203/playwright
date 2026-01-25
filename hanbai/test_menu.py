from playwright.sync_api import Page, expect

def test_dashboard_visible(auth_page: Page):
    cookies = auth_page.context.cookies()
    print(cookies)
    auth_page.goto("https://demo.hanbai.vn/menu")
    expect(auth_page.locator("a").first).to_be_visible().to_be_visible()
