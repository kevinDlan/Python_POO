class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Dancer:
    def __init__(self,style):
        self.style = style


class Student(Human,Dancer):
    def __init__(self, name, age,style):
        Human.__init__(self,name, age)
        Dancer.__init__(self,style)


student = Student(name='KONE',age=18,style='Couper Décaler')

print(student.style)