# Task 7: Implement a class RangeDescriptor that ensures any value set within the class is within a predefined range (e.g., 1 to 100). Use this descriptor in a class Product to manage the price attribute.

class RangeDescriptor:
    minimum = 1
    maximum = 100
    @classmethod
    def validation(cls, arg):
        if cls.minimum > arg or arg > cls.maximum:
            raise ValueError("Price should be between $1 and $100")
        
    def __get__(self, instance, owner):
        return instance.__dict__.get("__price")
    
    def __set__(self, instance, value):
        self.validation(value)
        instance.__dict__["__price"] = value


class Product:
    price = RangeDescriptor()

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f'{self.product_name} : ${self.price}'
    
prod = Product("apple", 13)
print(prod)

prod.price = 121
print(prod)