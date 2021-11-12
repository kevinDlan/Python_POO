METHODS = ['Stripe','Paypal','Orange Money','Wave']
class Payment:
    def __init__(self,method):
        self.__method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, setMethod):
        if setMethod in METHODS :
            self.__method = setMethod
        else:
            print('The method that your are enter is not avaible. Try over !')

    @method.deleter
    def method(self):
        self.__method = ''


pay = Payment('Stripe')
pay.method = 'Orange'

print(pay.method)

    