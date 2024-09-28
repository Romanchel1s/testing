class ProductPage:
    def __init__(self, page):
        self.page = page
        self.item_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")

    def add_to_cart(self):
        self.item_button.click()
        self.cart_button.click()