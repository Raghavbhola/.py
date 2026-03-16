#Interfaces - A class can implement multiple interfaces, which are defined as abstract base classes. An interface is a contract that specifies the methods that a class must implement.
#             In Python, we can use the abc module to define abstract base classes and interfaces.

# the only difference between an abstract class and an interface is that an abstract class can have both abstract and concrete methods, while an interface can only have abstract methods.
#  In Python, we can use the abc module to define both abstract classes and interfaces.

#2 types of interfaces in python
# 1. Formal Interface - A formal interface is defined using the abc module, and it is enforced by the language. 
#                       A class that implements a formal interface must implement all the methods defined in the interface. For example, we can define a formal interface for a class that represents a shape:
# 2. Informal Interface - An informal interface is a convention that specifies the methods that a class should implement. 
#                         It is not enforced by the language, and there is no way to check if a class implements an informal interface. 
#                         For example, we can define an informal interface for a class that represents a shape:

#formal Interface:
#(1)------------->
from abc import ABC , abstractmethod #abstruct base class
import abc
class Interface1(ABC):
    @abstractmethod
    def method1 (self):
        pass
    @abstractmethod
    def method2 (self):
        pass
class Interface2(ABC):
    @abstractmethod
    def method2 (self):
        pass

class kunalClass(Interface1,Interface2):
    def method1(self):
        #pass
        print("Implementation of method1")
    def method2(self):
        print("Implementation of method2")
    def method3(self):
        print("Implementation of method3")    

obj = kunalClass()
#obj1 = Interface1()  #This will give an error becoz we cannot instantiate an abstruct class
obj.method1()
obj.method2()   
obj.method3()          
       
#(2)--------------------------->
from abc import ABC , abstractmethod #abstruct base class
import abc
class Interface1(ABC):
    @abstractmethod
    def method1 (self):
        pass
    @abstractmethod
    def method2 (self):
        pass
class Interface2(ABC):
    @abstractmethod
    def method2 (self):
        pass

class kunalClass(Interface1,Interface2):
    def method1(self):
        #pass
        print("This is our system")
    def method2(self):
        print("BROH international ")
    def method3(self):
        print("It is Nature series")    

obj = kunalClass()
#obj1 = Interface1()  #This will give an error becoz we cannot instantiate an abstruct class
obj.method1()
obj.method2()   
obj.method3()          

#(3)------------------------>
class kunalClassInterface1:
    def method1(self):
        print("Kunal implementation of method1")

    def method3(self):
        print("Kunal implementstion of method3")

    def shubham(self):
        print("shubham implementation of method2")

obj2 = kunalClassInterface1()
obj2.method1()
obj2.method3()
obj2.shubham()

#Informal Interface -----------------
class demoInformalInterface:
    def method1(self):
        pass

    def method2(self):
        pass

class KunalClass(demoInformalInterface):
    def method1(self):
        print("Implementation of method1")
    def method2(self):
        print("Implementation of method2")
obj = KunalClass()
obj.method1()       #This will work because method1 is implemented
obj.method2()       #This will work because method2 is implemented

#Packages and Modules:- A package is a collection of modules, and a module is a file that contains Python code.
#                       A module can contain functions, classes, and variables. A package can contain sub-packages and modules. 
#                       In Python, we can use the import statement to import modules and packages.

#Inner Classes:- An inner class is a class that is defined inside another class. An inner class can access the members of the outer class, and it can also have its own members. 
#               Inner classes are used to logically group classes that are only used in one place, and they can also be used to hide the implementation details of a class.

#2 types of inner classes in python:-
#1st in multiple inner classes, we can have multiple inner classes inside an outer class. Each inner class can have its own members and methods, and they can also access the members of the outer class.
#2nd in multilevel inner classes, we can have inner classes inside inner classes. This allows us to create a hierarchy of classes that can access the members of the outer classes. 

#Anonymous class and objects:- An anonymous class is a class that is defined without a name. An anonymous object is an instance of an anonymous class. 
#                              Anonymous classes and objects are used when we need to create a class or an object that is only used once, and we do not want to give it a name. 
#                              In Python, we can use the lambda function to create anonymous functions, and we can use the type function to create anonymous classes.

class calculator:
    def __init__(self):
        self.result = 50
        return
c1 = calculator() 
print("Class of int",type(int))
print("Class of object",type(c1))
print("Class of class",type(calculator))
print("Class of Lambda",type(list()))   