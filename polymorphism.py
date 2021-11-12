class Language:
    def sayHello():
        raise NotImplemented('Please implement sayHello() methode in child instance')


class French(Language):
    def sayHello(self):
        print('Bonjour')

class English(Language):
    def sayHello(self):
        print('hello')
    
class Chiness(Language):
    def sayHello(self):
        print('China')


def intro(lang):
    lang.sayHello()


jhon = English()

lyon = French()

intro(jhon)
intro(lyon)