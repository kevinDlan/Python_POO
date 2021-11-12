# L'encapsulation consiste a rendre privé ou public les attribut et methode d'une classe.
class Payment:
    def __init__(self,price):
        self.__final_price = price + price*0.5

    def getFinalPrice(self):
        return self.__final_price


    def setFinalPrice(self,dis):
        self.__final_price = self.__final_price - self.__calculateDiscount(discount=dis)
    
    def __calculateDiscount(self,discount):
        return self.__final_price*(discount/100)

book = Payment(100)
book.setFinalPrice(dis=50)
# book.__calculateDiscount(10)
print('$',book.getFinalPrice())