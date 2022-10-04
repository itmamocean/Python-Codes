class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')
    def speak(self):
        print("I don't know what I say")

class Dog(Pet):

    def speak(self):
        print("meow")
    

class Cat(Pet):

    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("bark")

    def show(self):
        print(f'I am {self.name}, I am {self.age} and {self.color}')
    

c = Cat("Black", 19, "Cat")
 
c.show()
 
p = Pet("Tim", 14)
p.speak()
d = Dog("Bill", 15 )
d.speak()
