# Design a class ShoppingCart that encapsulates a private list of items (items). Implement methods to add an item, remove an item, and display the total number of items in the cart. Each item should have a name and price.

class Item:

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def result(self):
        return f'Product name: {self.product_name}\nPrice: {self.price}'

class ShoppingCart:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            print("ERROR")

    def remove_item(self, item_name):
        for i in self.__items:
            if i.product_name == item_name:
                self.__items.remove(i)
                return True
        return False
    
    def all_items(self):
        return len(self.__items)
    
    def information(self):
        if not self.__items:
            return "Shopping Cart is empty."
        item_info = "\n".join(item.result() for item in self.__items)
        return f'Shopping Cart:\n{item_info}'
    
if __name__ == "__main__":
    cart = ShoppingCart()
    apple = Item(product_name="apple", price=10)
    orange = Item(product_name="orage", price=20)
    
    cart.add_item(apple)
    cart.add_item(orange)
    
    print(cart.all_items())
    print(cart.information())

    cart.remove_item("apple")
    
    print(cart.all_items())
    print(cart.information())