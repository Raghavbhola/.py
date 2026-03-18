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


#wrapper class:- A wrapper class is a class that is used to wrap another class. A wrapper class can be used to add additional functionality to a class, or it can be used to modify the behavior of a class. 
#               In Python, we can use the decorator pattern to create wrapper classes.

def wrapper(class_to_wrap):
    class WrapperClass:
        def __init__(self,name, *args, **kwargs):
            self.wrapped_instance = class_to_wrap(name, *args, **kwargs)

        def getattr(self, name):
            return getattr(self.wrapped_instance, name)
    return WrapperClass

@wrapper
class MyClass:
    def __init__(self, x, *args, **kwargs):
        self.name = x

obj = MyClass("Kunal")
print(obj.wrapped_instance.name) # Output: Kunal
obj1 = MyClass("Krishna", 20)
print(obj1.wrapped_instance.name) # Output: Krishna
obj2 = MyClass("Satyam", 20, 30)
print(obj2.wrapped_instance.name) # Output: Satyam
obj3 = MyClass("shivam", 20, 30, 40, age = 25, gender = "Male")
print(obj3.wrapped_instance.name) # Outpput: shivam
            

#Singleton class:- A singleton class is a class that can only have one instance. A singleton class is used when we want to ensure that there is only one instance of a class, and we want to provide a global point of access to that instance. 
#                  In Python, we can use the __new__ method to create a singleton class.

#WAP to make a DB connection class a singleton class.

#CRUD operations:- CRUD stands for Create, Read, Update, and Delete. CRUD operations are the basic operations that can be performed on a database. 
#                  In Python, we can use the sqlite3 module to perform CRUD operations on a SQLite database.

#Enum:- Enum is a data type that consists of a set of named values. An enum can be used to represent a fixed set of constants, such as the days of the week, the months of the year, or the colors of the rainbow. 
#       In Python, we can use the enum module to create enums.

#Data classes:- A data class is a class that is used to store data. A data class is a simple class that has no behavior, and it is used to represent a data structure. 
#               In Python, we can use the dataclasses module to create data classes.
#               it helps for automatically generating special methods like __init__, __repr__, __eq__, etc. for a class. This can save us a lot of time and effort when we need to create classes that are primarily used to store data. 
#               For example, we can create a data class to represent a point in 2D space:

#(1)-------------------->
from dataclasses import dataclass

@dataclass
class PythonClasses:
    name : str
    age : int
    attendence : float= 0.0
    gender : str = "Not specified"

p1 = PythonClasses("Kunal",25, 90.5, "Male")
print(p1)
p2 = PythonClasses("Yashika", 34, 89.0,"Female")
print(p2)
p3 = PythonClasses("Akash", 28)
print(p3)
p4 = PythonClasses("Anjali", 27, 92.0)
print(p3)

print(p1.name)      #kunal
print(p2.age)       #34
print(p1 == p2)     #False

#(2)--------------->
#dataclass with mutable field:
from dataclasses import dataclass, field 

@dataclass
class PythonClasses:
    name : str
    age : int
    student_indo : list = field(default_factory = list)

p1 = PythonClasses("Kunal",25)
p1.student_indo.append("Student1")
print(p1)

