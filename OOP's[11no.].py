# OOP's[Object Oriented Program]
# Defn:->To map with real world scenarios, we started using objects in code. This is called OOP's

#NOTE- OOP is a approach not a coding.
#      OOP's are aapproach of programming or We tie him up as an object.
#      OOP's a POL i.e.[Paradigm] it is approach/concept.
#POL:->Procedural Oriented program Paradigm (program describes procedure of performing certain task ny written a series of instruction in a logical order)

#*Class & Object:-> *class is a blue print for creating objects.
#                 Ex:->   #creating class
#                      Class student:
#                         name="Karan Kumar"
#*Object refers to a real-world entity with state and behavior.
# Attribute+Behavior:->single-unit millke banati hai class

#Principle of OOP's:->
#(1)class
#(2)object
#(3)Encapsulation
#(4)Inheritance
#(5)Polymorphism
#(6)Abstruction 

# _init_ :-> initialization (its parameter self hi hoga)
#constructor:-All classes have a function called _init_(), which is always executed when the object is being initiated.

#First concept of OOP:classes and objects:->
#(1)----------->
class Employee:
    #Constructor to initialize the object
    employee_count=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.employee_count += 1

    #Method to diploy employee details
    def display_info(self):
        print(f"Name:{self.name},Position:{self.position},salary:{self.salary}")

    def display_count():
        print(f"Total Employee:{Employee.employee_count}")


#class object attribute
e1=Employee("Alice","Developer",70000)
e2=Employee("Bob","Designer",65000)
e3=Employee("Charlie","Manager",80000)
e4=Employee("Diana","Intern",30000)
e5=Employee("Ethan","Analyst",60000)

print(e1.salary)  #Accessing attributes of objects e1

e1.display_info()
e2.display_info()
e3.display_info()
e4.display_info()
Employee.display_count()                 


#print(e1.salary)  #Accessing attributes of objects e1

e1.display_info()
e2.display_info()
e3.display_info()
Employee.display_count()                

print(type(e1))      #output:<class'_main_.Employe'

#(2)------------->
class Employee:
    #constructer to intialize the object
    Employee_count = 0
    def __init__(abc,name,position,salary,age,city,experience):
        abc.name=name
        abc.position=position
        abc.salary=salary
        abc.age=age
        abc.city=city
        abc.experience=experience
        Employee.Employee_count +=1

#Method to display employee details
    def display_info(abc):
        print(f"Name:{abc.name},position:{abc.position},salary:${abc.salary},Age:{abc.age},city:{abc.city},experience:{abc.experience}")

    def display_count():
        print(f"Total Exployee:{Employee.Employee_count}")
    
#class objects attribute
e1=Employee("Alice","Developer",70000,30,"New York",5)
e2=Employee("Bob","Designer",65000,28,"San francise",4)
e3=Employee("Charlie","Manager",80000,35,"Chicago",10)           
e4=Employee("Diana","Intern",30000,22,"Boston",1)
e5=Employee("Ethan","Analyst",60000,27,"seatle",3)

e1.display_info()
e2.display_info()
e3.display_info()
e4.display_info()
e5.display_info()     

# to get delete
delattr(e3,'position')


e1.salary =30  #Dynamically additing attribution to object e1
e2.position="Design"

del e1.position

print(type(e1))
print(e2)
print(e1)
print(type(e2))
print(e3)
print(e4)

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__base__)
print(Employee.__bases__)
print(Employee.__dict__)

Flag_check= hasattr(e1,'Salary')  #check if e1 has attribute'salary'
print(Flag_check)  #False
Flag_check= hasattr(e3,'position') #check if e3 has attribute'position'
print(Flag_check)  #True

setattr(e2,'salary',7000) #setattribute 'salary' of e2 to 7000
e2.display_info()
getattr(e3,'position')
delattr(e4,'position')
e5.display_count

class Employee:
    #constructer to intialize the object
    Employee_count = 0
    def __init__(abc,name,position,salary,age,city,experience):
        abc.name=name
        abc.position=position
        abc.salary=salary
        abc.age=age
        abc.city=city
        abc.experience=experience
        Employee.Employee_count +=1

#Method to display employee details
    def display_info(abc):
        print(f"Name:{abc.name},position:{abc.position},salary:${abc.salary},Age:{abc.age},city:{abc.city},experience:{abc.experience}")

    def display_count():
        print(f"Total Exployee:{Employee.Employee_count}")
    
#class objects attribute
e1=Employee("Alice","Developer",70000,30,"New York",5)
e2=Employee("Bob","Designer",65000,28,"San francise",4)
e3=Employee("Charlie","Manager",80000,35,"Chicago",10)           
e4=Employee("Diana","Intern",30000,22,"Boston",1)
e5=Employee("Ethan","Analyst",60000,27,"seatle",3)

e1.display_info()
e2.display_info()
e3.display_info()
e4.display_info()
e5.display_info()

# to get delete
delattr(e2,'position')
     
e1.salary=30  #Dynamically additing attribute to object e1
e2.position="Design"

del e1.position


Flag_check= hasattr(e1,'Salary')  #check if e1 has attribute'salary'
print(Flag_check)  #False
Flag_check= hasattr(e3,'position') #check if e3 has attribute'position'
print(Flag_check)  #True

setattr(e2,'salary',7000) #setattribute 'salary' of e2 to 7000
e2.display_info()
getattr(e3,'position')
delattr(e4,'position')
e5.display_count

#---------------------------------->
class sample:
    _hidden_variable=0
    def count(self):
        self._hidden_variable +=10
        return self._hidden_variable
    
s1=sample()
s2=sample()
print(s2.count())     #10
print(s2.count())     #20
print(s1.count())     #10
print(s2.count())     #30
print(s1.count())     #20
print(s2.count())     #40
print(s1.count())      #30
print(s2.count())      #50
print(s2.count())      #60
print(s2.count())      #70
print(s2.count())      #80
print(s2.count())      #90
print(s2.count())      #100


#print(s1._sample_hidden_variable)
print(s1._hidden_variable)
print(s1._hidden_variable)

#------------------------------->
class sample:
    _hidden_variable=0
    def count(self):
        self._hidden_variable +=1000000898780000000
        return self._hidden_variable
    
s1=sample()
s2=sample()
print(s2.count())    #1000000898780000000
print(s2.count())    #2000001797560000000
print(s1.count())    #1000000898780000000
print(s2.count())    #3000002696340000000
print(s1.count())    #2000001797560000000

   
#print(s1._sample_hidden_variable)
#print(s1._hidden_variable)
#print(s1._hidden_variable)

#--------------------------------------------->
class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def display(self):
        print(f"print({self.x},{self.y})")

    def _del_(self):
        class_name=self.__class__.__name__
        print(f"{class_name} object is being destroyed")

p1=point()
p2=p1
p3=p2 
print(id(p1),id(p2),id(p3))       
del p1
del p2
del p3
#print(id(p1))

#--------------------------------------->
#Data hiding 
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number=account_number     #private attribute
        self._balance= balance                  #private attribute
    
    def depoist(self,ammount):
        if ammount > 0:
            self._balance+=ammount
            print(f"Depoisted:${ammount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self,ammount):
        if 0<ammount <= self._balance:
            self._balance-=ammount
            print(f"withdraw:${ammount}")
            print(f"Your account number{self._account_number} has been desited by {ammount}")
        else:
            print("Insufficient funds or invalid withdrawal ammount")

    def get_balance(self):
        print(f"Balance:${self._balance}")
b1= BankAccount("123456789",1000)
b1.withdraw(200)
b1.depoist(500)
b1.depoist(7864)
b1.get_balance()

print(b1._account_number)    #Acessing private attribute (not recommended)

#---------------------------------------->
class sample:
    _hidden_varaiable = 0
    def count(self):
        self._hidden_varaiable+=1
        return self._hidden_varaiable
    
s1= sample()
s2= sample()
print(s1.count())    #output:1
print(s2.count())    #output:1
print(s2.count())    #output:2
print(s1.count())    #output:2
#print(s1._sample_hidden_variable)    #attributeError
print(s1._hidden_varaiable)  #2
print(s2._hidden_varaiable)  #2

#------------------------
class sample:
    _hidden_varaiable = 0
    def count(self):
        self._hidden_varaiable+=10000067558000000
        return self._hidden_varaiable
    
s1= sample()
s2= sample()
print(s1.count())    
print(s2.count())    
print(s2.count())    
print(s1.count())    
#print(s1._sample_hidden_variable)    #attributeError
print(s1._hidden_varaiable)  
print(s2._hidden_varaiable)  

#----------------
class employee:
    name="Akash"
    age=30

class employee:
    name="Karan"
    age=5465    

e1= employee()
e2= employee()
print(e1.name,e2.name)  
print(e1.age,e2.age)    

#---------------------------------------->
class Employee:
    empcount=5   #class attribute
    def __init__(self,name="Akash",age=500):  #instance attribute
        self.name=name
        self.age=age
        Employee.empcount +=1
        print("Name=",name,",Age:-", age)
        print("Employee count is =",Employee.empcount)

e1=Employee("Shubham",1090)
e2=Employee("Karan")
e3=Employee("System",34)


#Methods:- Functions defined to perform a dedicated activity/operators.
#   Methods are divided into 3 categories
#   (1)Class Method
#   (2)Instance Method 
#   (3)Static Method

#NOTE:-const. is a class method
#(1)Class Method:-A python class method is a method that is bound to the class not to the instance of the class. it can be called on the class itself rather than on an instance of the class.
#(2)Instance method:-They have access to class and instance attributes.
#(3)Static method:-that method who have access to modify the state.
#         *constant-never change

class Employee:
    empcount=0   #class attribute
    def __init__(self,name="Akash",age=500):  #instance attribute
        self.name=name
        self.age=age
        Employee.empcount += 1
       
    @classmethod
    def showCount(self):
        print(self.empcount)

    @classmethod
    def newEmployee(self,name,age):
        return(self,name,age)

e1 = Employee("Shubham",109)
e2 = Employee("Karan",7)
e3 = Employee("System",34)

e1.showCount() 
#Employee.showCount(e1)
Employee.showCount()

#-------------------------
class Employee:
    empcount=0   #class attribute
    def __init__(self,name="Akash",age=30):  #instance attribute
        self.name=name
        self.age=age
        Employee.empcount += 1
       
    @classmethod
    def showCount(self):
        print(self.empcount)

    @classmethod
    def newEmployee(self,name,age):
        print(self,name,age)

e1 = Employee("Shubham", 19)
e2 = Employee("Karan", 70)
e3 = Employee("System", 34)
e4 = Employee("holla", 21)

e1.showCount() 
#Employee.showCount(e1)
Employee.showCount()
e2.showCount()

#-----------------------
class Karan :
    money=400000  #class attribute

    @classmethod
    def showmoney(kunal):
        return kunal.money

print(Karan.showmoney())    
#---------------------------
class Karan :
    money=1000000000000 #class attribute

    @classmethod
    def showmoney(kunal):
        return kunal.money

print(f"karan show money:-",Karan.showmoney())    #karan show money:- 1000000000000



#Constructors:-> Its an instance method in a class, automatically called whenever a new object of the class is created.
#            --> its role is to assign value to the instance variable as soon as object is created. it needs a mandatory argument "self"
#  There are two types of constructors:->(1)Default constructor
#                                        (2)Parameterized constructor

#-------------------------------
class Employee:
    def __init__(self):      #default constructer
        self.name = "Bhawana"
        self.age  = 30
        self.salary = 50000

e1 = Employee()
e2 = Employee()
e3 = Employee()

print(e3.name)
print(e1.age)
print(e2.salary)

#-------------------------
class Employee:
    def __init__(self):      #default constructer
        self.name = "yamunaa"
        self.age  = 30
        self.salary = 100000000

e1 = Employee()
e2 = Employee()
e3 = Employee()

print(e3.name)
print(e1.age)
print(e2.salary)

#Inheritance:->Reusability is one of the key benefits of object oriented programming (OOPs). 
#              Instead of writing code again and again, we can reuse existing tested classes.
#              This saves times, effort, money, & reduces errors.
# The existing class is called the base class (or parent class), of the new class is called Derived class(or child class).

# There are 5 types of Inheritance:-
#                    (1)Single inheritance
#                    (2)Multilevel inheritance
#                    (3)Multiple inheritance
#                    (4)Hierarchinal inheritance
#                    (5)hybrid inheritance

#Single inheritance:->>
#(1)---------------
class Parent:
    def greet (self):
        return "Hello from parent"
    def greet1 (self):
        return "Good morning from parent"
    def greet2 (self):
        return "Good night from parent"
    
class child (Parent):
    def greet_child(self):
        return "hello from child"

c1 = child()
print(c1.greet_child())
print(c1.greet()) 
print(c1.greet1())
print(c1.greet2())

#(2)-----------------------------------------------------
class vehicle:
    def name (self):
        return"This is my Porsche"
    def name1 (self):
        return"This is my BMW"
    
class car(vehicle):
    def name_car (self):
        return"hello"

c1 = car()
print(c1.name_car())
print(c1.name())        
print(c1.name1())

#(3)--------------------------------------------------------
class parent:
    def parent_mothod(Yashika, name ="Akash",age = 40):
        Yashika = name
        Yashika = age
        return "This is method in the Parent class.Name: {}, Age:{}".format(name,age)
    
class child (parent):
    def child_method(yashika, name = "Akash", age = 30):
        yashika.name = name
        yashika.age = age
        return "This is a method in the child.Name: {}, Age:{}".format(name,age)

c1 = child()
p1 = parent()
print(c1.parent_mothod())
print(c1.child_method())        


#Multiple inheritance:--------------------------------
#(1)-----------------------------
class Parent1:
    def method1(self):
        return"This is method 1 from Parent1"
    
class Parent2:
    def method2(self):
        return "This is method 2 from Parent2"

class parent3:
    def method1(self):
        return "This is method 3 from Parent3"    

class child(Parent2,parent3):
    def child_method(self):
        return"This is a method"
           

c1 = child()
print(c1.method1())
print(c1.method2())
print(c1.method1())
print(c1.child_method())

#NOTE:- MRO(Method Resolution Order):- The order in which python looks for a method in a hierarchy of classes.

#(1)-----------------------------------------------------
class Division:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def divide(self):
        if self.b != 0:
            return self.a/self.b
        else:
            return"Cannot divide by zero"

class Modulos:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def modulos(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return"cannot modulos by zero"    

class calculator(Division, Modulos):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculator_method(self):
        divval = Division.divide(self)  
        modval = Modulos.modulos(self)
        return"Division: {}, Modulos: {}".format(divval,modval)

a = 16
b = 78
c1 = calculator(a,b)
print("Division and Modulos:",c1.calculator_method())
print("Division:",c1.divide())
print("Modulos:",c1.modulos())                     

#(2)---------------------------------------------------
class Division:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def divide(self):
        if self.b != 0:
            return self.a/self.b
        else:
            return"Cannot divide by zero"

class Modulos:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def modulos(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return"cannot modulos by zero"    

class calculator(Division, Modulos):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculator_method(self):
        divval = Division.divide(self)  
        modval = Modulos.modulos(self)
        return"Division: {}, Modulos: {}".format(divval,modval)

a = int(input("enter the number"))
b = int(input("enter the number"))
c1 = calculator(a,b)
print("Division and Modulos:",c1.calculator_method())
print("Division:",c1.divide())
print("Modulos:",c1.modulos())             

#Multilevel Inheritance:->

class Grandparent:
    def grandparent_method(Self):
        return"This is a method in the Grandparent class"

class Parent(Grandparent):
    def parent_method(self):
        return"This is a method in the parent class"

class child(Parent):
    def child_method(self):
        return"This is a method in the child class"

class Futurechild(child):
    def future_child_method(self):
        return"This is a method in the future child class"
    
c1 = Futurechild()
print(c1.future_child_method())
print(c1.child_method())
print(c1.parent_method())
print(c1.grandparent_method())   
print("------------------------------------------")

c2 = child()
print(c2.child_method())
print(c2.parent_method())
print(c2.grandparent_method())

#-----------------------------------
class Grandparent:
    def grandparent_method(Self):
        return"Grandparent class"

class Parent(Grandparent):
    def parent_method(self):
        return"parent class"

class child(Parent):
    def child_method(self):
        return"child class"

class Futurechild(child):
    def future_child_method(self):
        return"future child class"
    
c1 = Futurechild()
print(c1.future_child_method())
print(c1.child_method())
print(c1.parent_method())
print(c1.grandparent_method())
print("------------------------------------------")

c2 = child()
print(c2.child_method())
print(c2.parent_method())
print(c2.grandparent_method())

#(4)Hierarchinal Inheritance:->

class Parent:
    def parent_method(self):
        return"This is a method in the parent class"     

class child1(Parent):
    def child1_method(self):
        return"This is a method in the child1 class"

class child2(Parent):
    def child2_method(self):
        return"This is a method in the child2 class" 

class child3(Parent):
    def child3_method(self):
        return"This is a method in the child3 class" 

c1 = child1()
c2 = child2()
c3 = child3()

print(c1.parent_method())
print(c2.child2_method())
print(c3.child3_method())
print(c2.child2_method())
print("-------------------------------------")
print(c3.parent_method())
print(c3.child3_method())


#Hybrid Inheritance:-> A combination of two or more types of inheritance.

class CEO:
    def method_ceo(self):
        return"This is method 1 from CEO"

class Manager(CEO):
    def method_manager(self):
        return"This is method 2 from Manager"

class Employee(CEO):
    def method_employee(self):
        return"This is method 3 from Employee"

class Intern(Employee,Manager):
    def child_method(self):
        return"This is a method in the child class"

i1 = Intern()
print(i1.child_method())
print(i1.method_ceo())
print(i1.method_manager())
print(i1.method_employee())                
