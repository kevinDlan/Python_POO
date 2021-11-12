# Basic class creation
class Book:
    # class constructor
    def __init__(self,name,author,create_year):
        self.name = name
        self.author = author
        self.create_year = create_year
    
    def setName(self,name):
        self.name = name
    
    def getName(self):
        if self.name != '':
            return self.name
        else:
            return 'Notting setting yet'


book = Book(name='',author='Nick',create_year='2021')

print(book.getName())