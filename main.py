import random


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Stock: {self.stock})"

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            print(f"Not enough stock for {self.name}.")
            return False

    def increase_stock(self, quantity):
        self.stock += quantity


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.reduce_stock(quantity):
            if product.name in self.items:
                self.items[product.name] += quantity
            else:
                self.items[product.name] = quantity
            print(f"Added {quantity} of {product.name} to the cart.")
            self.print_cart()
        else:
            print(f"Could not add {product.name} to the cart due to stock issues.")

    def remove_product(self, product, quantity):
        if product.name in self.items:
            if self.items[product.name] >= quantity:
                self.items[product.name] -= quantity
                product.increase_stock(quantity)
                if self.items[product.name] == 0:
                    del self.items[product.name]
                print(f"Removed {quantity} of {product.name} from the cart.")
                self.print_cart()
            else:
                print(f"Cannot remove {quantity} of {product.name}; only {self.items[product.name]} in cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for product_name, quantity in self.items.items():
            total += quantity * products[product_name].price

        # Apply random discount
        discount = random.uniform(0, 0.2)
        total_with_discount = total * (1 - discount)
        print(
            f"Total before discount: ${total:.2f}, Discount: {discount * 100:.1f}%, Total after discount: ${total_with_discount:.2f}")
        return total_with_discount

    def print_cart(self):
        print("Current items in the cart:")
        for product_name, quantity in self.items.items():
            print(f"{quantity} x {product_name}")
        print()


# Example products
products = {
    "Laptop": Product("Laptop", 999.99, 10),
    "Phone": Product("Phone", 499.99, 20),
    "Headphones": Product("Headphones", 199.99, 15),
    "Tablet": Product("Tablet", 299.99, 25),
    "Smartwatch": Product("Smartwatch", 199.99, 30),
    "Camera": Product("Camera", 499.99, 5),
    "Printer": Product("Printer", 149.99, 10),
    "Monitor": Product("Monitor", 249.99, 8),
    "Keyboard": Product("Keyboard", 49.99, 50),
    "Mouse": Product("Mouse", 29.99, 40),
    "Gaming Console": Product("Gaming Console", 299.99, 12),
    "Bluetooth Speaker": Product("Bluetooth Speaker", 89.99, 25),
    "External Hard Drive": Product("External Hard Drive", 119.99, 15),
    "USB Flash Drive": Product("USB Flash Drive", 19.99, 100),
    "Smart TV": Product("Smart TV", 799.99, 7),
    "Drone": Product("Drone", 599.99, 8),
    "VR Headset": Product("VR Headset", 399.99, 5),
    "Electric Scooter": Product("Electric Scooter", 499.99, 4),
}

# Create cart and add random products
cart = Cart()
num_products_to_add = random.randint(1,
                                     len(products) // 2)
for _ in range(num_products_to_add):
    product = random.choice(list(products.values()))
    quantity = random.randint(1, 3)
    cart.add_product(product, quantity)

# Randomly remove a product from the cart
if cart.items:
    product_to_remove = random.choice(list(cart.items.keys()))
    quantity_to_remove = random.randint(1, cart.items[product_to_remove])
    cart.remove_product(products[product_to_remove], quantity_to_remove)

# Calculate total
total_price = cart.calculate_total()
