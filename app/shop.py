from app.customer import Customer
from app.distance import Distance
import datetime


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        self.dict_products = {}
        self.cost = 0
        self.distance = 0
        self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def price_products(self, customer_product: Customer) -> int:
        for product in customer_product.product_cart:
            price_for_product = (customer_product.product_cart[product]
                                 * self.products[product])
            self.dict_products.update({product: [
                price_for_product,
                customer_product.product_cart[product]]})
            self.cost += price_for_product
        distance = Distance(customer_product, self.location)
        self.cost += distance.distance_between()
        self.distance += distance.distance_between()
        print(f"{customer_product.name}'s "
              f"trip to the {self.name} costs {self.cost}")
        return self.cost
