class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.locator('#login-button')
        self.title = page.get_by_text("Swag Labs")
        self.error_message = page.locator('h3[data-test="error"]')
    
    def navigate(self):
        self.page.goto("https://www.saucedemo.com")
    
    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
    def get_error_message(self):
        return self.error_message