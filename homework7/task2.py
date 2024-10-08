from abc import ABC, abstractmethod

# MenuItem Class
class MenuItem:
    __slots__ = ('_name', '_price', '_ingredients')

    def __init__(self, name, price, ingredients):
        self._name = name
        self._price = price
        self._ingredients = ingredients

    def show_menu(self):
        return f'NAME : {self._name}\nPRICE : {self._price}\nINGREDIENTS : {self._ingredients}'

# Appetizer subclass
class Appetizer(MenuItem):
    __slots__ = ('_serving_size',)

    def __init__(self, name, price, ingredients, serving_size):
        super().__init__(name, price, ingredients)
        self._serving_size = serving_size
    
    def show_menu(self):
        main_menu = super().show_menu()
        return f'{main_menu}\nSERVING SIZE : {self._serving_size}'
    
# Entree subclass
class Entree(MenuItem):
    __slots__ = ('_cooking_method',)

    def __init__(self, name, price, ingredients, cooking_method):
        super().__init__(name, price, ingredients)
        self._cooking_method = cooking_method
    
    def show_menu(self):
        main_menu = super().show_menu()
        return f'{main_menu}\nCOOKING METHOD : {self._cooking_method}'

# Dessert subclass 
class Dessert(MenuItem):
    __slots__ = ('_calories',)

    def __init__(self, name, price, ingredients, calories):
        super().__init__(name, price, ingredients)
        self._calories = calories
    
    def show_menu(self):
        main_menu = super().show_menu()
        return f'{main_menu}\nCALORIES : {self._calories}'
    

# Customer Class
class Customer:
    __slots__ = ('_name', '_contact_info', '_order_history')

    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._order_history = []

    def place_order(self, order):
        self._order_history.append(order)

    def view_order_history(self):
        if not self._order_history:
            return "You have no order history"
        else:
            return self._order_history

    def customer_info(self):
        return f'CUSTOMER NAME : {self._name}\nCONTACT INFO : {self._contact_info}'


# Order Abstract class
class Order(ABC):
    __slots__ = ('_customer', '_menu_items', '_total_price')

    def __init__(self, customer):
        self._customer = customer
        self._menu_items = []
        self._total_price = 0

    def add_menu_item(self, menu_item):
        self._menu_items.append(menu_item)
        self._total_price += menu_item._price

    @abstractmethod
    def get_order_type(self):
        ...

    def view_order_details(self):
        return f"ORDER TYPE: {self.get_order_type()}\nITEMS:\n{self._menu_items}\nTOTAL PRICE: ${self._total_price}"



class TakeawayOrder(Order):
    __slots__ = ()

    def get_order_type(self):
        return "Takeaway"


class DeliveryOrder(Order):
    __slots__ = ('_delivery_address',)

    def __init__(self, customer, delivery_address):
        super().__init__(customer)
        self._delivery_address = delivery_address

    def get_order_type(self):
        return "Delivery"

    def view_order_details(self):
        """Overrides to include delivery address."""
        base_details = super().view_order_details()
        return f"{base_details}\nDelivery Address: {self._delivery_address}"
    
# Review class

class Review:
    __slots__ = ('_customer_name', '_order', '_rating', '_comments')

    def __init__(self, customer_name, order, rating, comments):
        self._customer_name = customer_name
        self._order = order
        self._rating = rating
        self._comments = comments

    def display_review(self):
        return (f"Review by: {self._customer_name}\n"
                f"Order: {self._order}\n"
                f"Rating: {self._rating}/5\n"
                f"Comments: {self._comments}")


# Usage

appetizer = Appetizer("Bruschetta", 6.99, ["bread", "tomatoes", "basil"], "2 pieces")
entree = Entree("Grilled Salmon", 18.99, ["salmon", "lemon", "herbs"], "Grilled")
dessert = Dessert("Chocolate Cake", 5.49, ["flour", "chocolate", "sugar"], 350)

print(appetizer.show_menu())

person = Customer("Nancy", "099123456")
order = person.place_order("Bruschetta")
print(person._order_history)

review = Review("Nancy", "Bruschetta", 5, "Great!")
print(review.display_review())

