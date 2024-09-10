# Design a class Product with private attributes product_id, product_name, and quantity_in_stock. Implement methods to set and get the values of these attributes and to adjust the quantity_in_stock (e.g., adding stock or reducing stock).

class Product:

    def __init__(self, product_id, product_name, quantity_in_stock):

        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def set_product_id(self, product_id):
        self.__product_id = product_id
    
    def get_product_id(self):
        return self.__product_id
    
    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name
    
    def set_quantity_in_stock(self, quantity_in_stock):
        self.__quantity_in_stock = quantity_in_stock

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock
    
    def add_stock(self, amount):
        if amount >= 0:
            self.__quantity_in_stock += amount
        else:
            print("Amount shoul be positive")

    def reduce_stock(self, amount):
        if amount >= 0:
            if amount <= self.__quantity_in_stock:
                self.__quantity_in_stock -= amount
            else:
                print("Amount should be less than quantitiy")
        else:
            print("Amount should b positive number")



if __name__ == "__main__":
    item = Product(123, "Jeans", 20)
    print(f'Product ID: {item.get_product_id()}\nName: {item.get_product_name()}\nQuantity: {item.get_quantity_in_stock()}')

    item.reduce_stock(12)
    print(f'Updated stock: {item.get_quantity_in_stock()}')

    item.add_stock(14)
    print(f'Updated stock: {item.get_quantity_in_stock()}')

    item.add_stock(-12)

