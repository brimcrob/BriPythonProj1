class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour


    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.colour} in colour")


class Dog(Pet):
    def speak(self):
        print("Woof")


class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill", 25)
d.speak()
f = Fish("Bubbles", 10)
f.speak()

