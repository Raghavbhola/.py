#Polymorphism:-> The ability of a function or method to take on many forms. it allows us to same mathod name for different types of objects.

#NOTE:->Its very easy to acheive polymorphism in Python because of its dynamic typing and duck typing features. We can use the same method name for different types of objects and it will work based on the type of object.
#        We can also achieve polymorphism by using inheritance and method overriding.

#1. Function Overriding - When a method in a child class has the same name as a method in the parent class, the method in the child class overrides the method in the parent
#2. Operator Overloading - When a operator is used with different types of objects, it behaves differently based on the type of object.
#3. Function Overloading - When a function is defined with the same name but different parameters, it is called function overloading. Python does not support function overloading, but we can achieve it by using default parameters or variable length arguments.
#4. Duck typing - When the type of an object is determined by its behavior rather than its class. It is based on the principle of "If it looks like a duck and quacks like a duck, then it is a duck". It allows us to use objects of different classes in the same way if they have the same behavior.

#(1)Duck Typing:->
class duck:
    def quack(self):
        return"Quack Quack"
    def fly (self):
        return"I am flying"

class AnotherBird:
    def quack(self):
        return"I am not a duck but I can quack like a duck"
    def fly(self):
        return"I am flying too"
    def makeSound(bird):
        print(bird.quack())
        print(bird.fly())

duck1 = duck()
bird1 = AnotherBird()
AnotherBird.makeSound(bird1)
AnotherBird.makeSound(duck1)


class Dog:
    def sound(self):
        return "Bark"
    def scratch(self):
        return"Fetching the ball"
class cat:
    def sound(self):
        return"Meow"
    def scratch(self):
        return"Scratching the furniture"
    def animal_sound(self):
        print(self.sound())
        print(self.scratch())

class Human:
    def sound(self):
        return"Hello"
    def scratch(self):
        return"Typing on the keyboard"
    def Human_method(self):
        print(self.sound())
        print(self.scratch())

c1 = cat()
d1 = Dog()
h1 = Human()
Human.Human_method(d1)
Human.Human_method(c1)
Human.Human_method(h1)
