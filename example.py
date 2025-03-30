from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 將 headless 設定為 False
    page = browser.new_page()
    page.goto('https://example.com')
    page.wait_for_timeout(2000)  # 等待 2 秒
    print('等待結束')
    page.screenshot(path="example.png")
    browser.close()
