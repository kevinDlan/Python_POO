class Polygon:
    def __init__(self,sides):
        self.sides = sides

    def area(self,lenght):
        return lenght**2

class Square(Polygon):
    def __init__(self, sides,perimeter):
        super().__init__(sides)
        self.perimeter = perimeter

class Triangle(Polygon):

    # Override method from parent class
    def area(self, lenght,base):
        return 0.5*lenght*base


sq = Square(sides=4,perimeter=10)

# print(isinstance(sq,Square))

# print(issubclass(Triangle,Polygon))

# print(sq.area(lenght=5))

print(sq.sides, sq.perimeter)