class Book:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self,other):
        return self.price + other.price

    def __lt__(self,other):
        return self.price<other.price

    
book1 = Book('All About Dart','$150')
book2 = Book('Learn JS','$200')
compare = book1>book2

total_price = book1 + book2
# Make a addition
# print(int.__add__(10,12))
# print(int.__sub__(15,10))
print(compare)