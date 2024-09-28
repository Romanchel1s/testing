class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_ = page.locator("[data-test=\"checkout\"]")
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_shopping = page.locator("[data-test=\"continue\"]")
        self.finish_ = page.locator("[data-test=\"finish\"]")
        self.succes_message = page.locator("[data-test=\"complete-header\"]")

    def checkout(self):
        self.checkout_.click()

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def finish(self):
        self.continue_shopping.click()
        self.finish_.click()
    
    def get_succes_message(self):
        return self.succes_message