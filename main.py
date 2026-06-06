import unittest

# --- WARSTWA DOMENY

class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.items.append((product, quantity))
        else:
            raise ValueError(f"Brak wystarczającej ilości produktu {product.name} na magazynie.")

    def get_total_value(self):
        return sum(product.price * quantity for product, quantity in self.items)


# --- WARSTWA SERWISÓW

class OrderService:
    def create_order(self, cart):
        if not cart.items:
            raise ValueError("Koszyk jest pusty. Nie można złożyć zamówienia.")
        
        total_amount = cart.get_total_value()
        

        for product, quantity in cart.items:
            product.stock_quantity -= quantity
            
        return {
            "status": "Nowe",
            "total_amount": total_amount,
            "message": "Zamówienie zostało pomyślnie utworzone."
        }


# --- TESTY JEDNOSTKOWE

class TestOrderService(unittest.TestCase):
    
    def test_create_order_calculates_correct_total_and_updates_stock(self):

        laptop = Product(product_id=1, name="Laptop", price=3500.00, stock_quantity=10)
        myszka = Product(product_id=2, name="Myszka", price=150.00, stock_quantity=50)
        
        cart = ShoppingCart()
        cart.add_product(laptop, 1)  
        cart.add_product(myszka, 2) 
        
        service = OrderService()
        

        order_result = service.create_order(cart)
        

        self.assertEqual(order_result["total_amount"], 3800.00)
        self.assertEqual(order_result["status"], "Nowe")
        self.assertEqual(laptop.stock_quantity, 9)

if __name__ == '__main__':
    unittest.main()
