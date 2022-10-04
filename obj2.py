class Car:
    def __init__(self, n,c):

        self.name = n
        self.color = c

    def start(self):
        print("name: ", self.name)
        print("color: ", self.color)
        print("Starting the engine") 
my_car1 = Car("premio", "white")
my_car1.start()
my_car2 = Car("allion", "blue")
my_car2.start()
my_car1.year = 2017
print(my_car1.name, my_car1.color, my_car1.year)


        