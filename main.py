from playwright.sync_api import sync_playwright

app = sync_playwright().start()
browser = app.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
def get_js_hook() -> str:
    with open('main.js', 'r', encoding='utf-8') as f:
        return f.read()
# 注入脚本
page.add_init_script(get_js_hook())
# 淘宝登录尝试
# page.goto("https://login.taobao.com/member/login.jhtml")
# 环境检测网页
page.goto("https://bot.sannysoft.com/")
input()
browser.close()
app.stop()