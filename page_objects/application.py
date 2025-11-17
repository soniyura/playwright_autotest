from playwright.sync_api import Playwright # Импорт Playwright для взаимодействия с браузером


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless = False):
        self.browser = playwright.chromium.launch(headless = headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def goto(self, endpoint: str, use_base_url = True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)


    def navigate_to (self, menu: str):
        self.page.click(f"css=header >> text=\"{menu}\"")


    def login(self, login: str, password: str):
        self.page.get_by_role("textbox", name="Username:").fill(login)
        #self.page.get_by_role("textbox", name="Password:").click()
        self.page.get_by_role("textbox", name="Password:").fill(password)
        self.page.get_by_role("button", name="Login").click()


    def create_test(self, test_name: str, test_description: str):
        self.page.locator("#id_name").fill(test_name)
        self.page.get_by_role("textbox", name="Test description").fill(test_description)
        self. page.get_by_role("button", name="Create").click()


    def check_test_exists(self, test_name: str):
        return self.page.query_selector(f'css=tr >> text=\"{test_name}\"') is not None


    def delete_test_by_name(self, test_name: str):
        row = self.page.query_selector(f'*css=tr >> text=\"{test_name}\"')
        row.query_selector('.deleteBtn').click()


    def close(self):
        #self.page.close()
        self.context.close()
        self.browser.close()