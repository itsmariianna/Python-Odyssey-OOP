# Design a class Book with private attributes title, author, and price. Create methods to set and get the values of these attributes. Ensure that the price cannot be set below a certain value (e.g., 10).

class Book:
    
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price if price >= 10 else 10

    def set_title(self, title):
        self.__title = title
    
    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author
    
    def set_price(self, price):
        if price >= 10:
            self.__price = price
        else:
            print("The price should be 10 or greater. Seting price to 10")
            self.__price = 10
            
    
    def get_price(self):
        return self.__price
    
if __name__ == "__main__":
    result = Book("Harry Potter", "J. K. Rowling", 100)
    print(f'Title: {result.get_title()}\nAuthor: {result.get_author()}\nPrice: {result.get_price()}')

    result.set_price(8)

    print(f'Updated price: {result.get_price()}')

