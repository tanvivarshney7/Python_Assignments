#1. Create a basic Car class
# Create a Car class with __init__ that takes brand and model. Add a method display_info() that prints
# both. Create two Car objects and call the method on each.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car1.display_info()
car2.display_info()


#2. Track number of objects created
# Create a class Counter with a class variable count starting at 0. Every time a new object is created,
# increase count by 1. Add a class method get_count() that returns the current count.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
a = Counter()
b = Counter()
c = Counter()
print(Counter.get_count())


#3.Rectangle area and perimeter
# Create a Rectangle class that takes length and width. Add methods area() and perimeter() that return
# the respective calculations.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
r = Rectangle(5,3)
print(r.area())
print(r.perimeter())


#4. Protect balance with a private attribute
# Create a BankAccount class with a private attribute __balance set in __init__. Add deposit(amount)
# and get_balance() methods. Do not allow direct access to __balance from outside the class.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())


#5. Animal and Dog inheritance
# Create a base class Animal with a method speak() that returns 'Some sound'. Create a Dog class that
# inherits from Animal and overrides speak() to return 'Bark'. Create one object of each and call speak().
class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Bark"
a = Animal()
d = Dog()
print(a.speak())
print(d.speak())


#6. Student class with default values
# Create a Student class where age defaults to 18 if not provided. The __init__ should accept name and
# an optional age parameter.
class Student:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
s1 = Student("Ali")
s2 = Student("Mia", 21)
print(s1.name, s1.age)
print(s2.name, s2.age)


#7. Use a property to validate age
# Create a Person class with a private attribute __age. Use the @property decorator to create a getter
# for age, and a setter that raises a ValueError if the age is negative.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value
p = Person("Sam", 25)
print(p.age)
try:
    p.age = -5
except ValueError as e:
    print(f"ValueError: {e}")


#8. Use super() to extend the parent constructor
# Create a Vehicle class with __init__ that sets brand. Create a Car class that inherits from Vehicle,
# adds a model attribute, and calls super().__init__() to set the brand.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
c = Car("Toyota", "Corolla")
print(c.brand, c.model)


#9. Same method name, different shapes
# Create a Shape base class with a method area() returning 0. Create Circle and Square subclasses
# that each override area() with their own formula. Loop through a list of shape objects and call area()
# on each.
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)   #used 3.14 instead of math.pi to match the output given in the assignment
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
shapes = [Circle(5), Square(4)]
for s in shapes:
    print(s.area())


#10. String representation using __str__
# Create a Book class with title and author. Override the __str__ method so that printing a Book object
# shows a formatted string instead of the default object representation.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"
b = Book("Dune", "Frank Herbert")
print(b)


#11. Three-level inheritance chain
# Create a class Vehicle with attribute wheels. Create Car that inherits from Vehicle and adds brand.
# Create SportsCar that inherits from Car and adds top_speed. Create a SportsCar object and print all
# three attributes.
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)
        self.brand = brand
class SportsCar(Car):
    def __init__(self, wheels, brand, top_speed):
        super().__init__(wheels, brand)
        self.top_speed = top_speed
sc = SportsCar(4, "Ferrari", 340)
print(sc.wheels, sc.brand, sc.top_speed)


#12. Method overriding with super() call
# Create an Employee class with a method calculate_bonus() returning 1000. Create a Manager
# subclass that overrides calculate_bonus() to call the parent's value using super() and adds an extra
# 2000 on top.
class Employee:
    def calculate_bonus(self):
        return 1000
class Manager(Employee):
    def calculate_bonus(self):
        return super().calculate_bonus() + 2000
e = Employee()
m = Manager()
print(e.calculate_bonus())
print(m.calculate_bonus())


#13. Inventory system with private stock
# Create a Product class with a private __stock attribute. Add methods sell(quantity) that reduces stock
# only if enough is available (otherwise print an error), and restock(quantity) that increases it. Add a
# method check_stock() to view current stock.
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock
    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print("Not enough stock!")
    def restock(self, quantity):
        self.__stock += quantity
    def check_stock(self):
        return self.__stock
p = Product("Pen", 50)
p.sell(20)
p.sell(40)
p.restock(15)
print(p.check_stock())


#14. Multiple subclasses sharing one parent method
# Create a base class Employee with __init__ for name and base_salary, and a method total_pay()
# returning base_salary. Create Developer and Designer subclasses, each overriding total_pay() to add
# a different fixed bonus on top of the base.
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def total_pay(self):
        return self.base_salary
class Developer(Employee):
    def total_pay(self):
        return self.base_salary + 5000
class Designer(Employee):
    def total_pay(self):
        return self.base_salary + 3000
d = Developer("Ali", 50000)
de = Designer("Mia", 45000)
print(d.total_pay())
print(de.total_pay())


#15. Polymorphism with a common interface
# Create a PaymentMethod base class with a method pay(amount) that raises NotImplementedError.
# Create CreditCard and PayPal subclasses that each implement pay() differently (different printed
# message). Loop through a list of payment objects and call pay() on each with the same amount.
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method")
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")
class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")
methods = [CreditCard(), PayPal()]
for m in methods:
    m.pay(100)


#16. Read-only property derived from private data
# Create a Circle class with a private __radius set in __init__. Add a read-only property called area that
# calculates and returns the area each time it is accessed — without storing it. Do not allow area to be
# set directly.
class Circle:
    def __init__(self, radius):
        self.__radius = (radius)
    @property
    def area(self):
        return 3.14 * self.__radius ** 2    #used 3.14 instead of math.pi to match the output given in the assignment
c = Circle(10)
print(c.area)
try:
    c.area = 500
except AttributeError:
    print("AttributeError: can't set attribute")


#17. Override and extend a method's behaviour
# Create a Shape class with a method describe() that returns 'This is a shape'. Create a Triangle
# subclass that overrides describe() to call the parent's describe() using super() and appends ' -
# specifically a triangle' to the result.
class Shape:
    def describe(self):
        return "This is a shape"
class Triangle(Shape):
    def describe(self):
        return super().describe() + " - specifically a triangle"
t = Triangle()
print(t.describe())


#18. Compare two objects using a custom method
# Create a Student class with name and score. Add a method called compare(other) that returns the
# name of whichever student (self or other) has the higher score. Use this method to compare two
# student objects.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def compare(self, other):
        if self.score > other.score:
            return self.name
        else:
            return other.name
s1 = Student("Ali", 85)
s2 = Student("Mia", 92)
print(s1.compare(s2))


#19. Duck typing without inheritance
# Create two unrelated classes, Duck and Robot, each with their own make_sound() method returning
# different strings. Without using a common parent class, loop through a list containing one of each and
# call make_sound() on every object — demonstrating that Python does not require inheritance for
# polymorphism.
class Duck:
    def make_sound(self):
        return "Quack!"
class Robot():
    def make_sound(self):
        return "Beep Boop!"
objects = [Duck(), Robot()]
for obj in objects:
    print(obj.make_sound())


#20. Build a class with full encapsulation and validation
# Create a Temperature class storing a private __celsius value. Provide a property celsius with a getter
# and a setter that raises a ValueError if the value is below -273.15 (absolute zero). Also add a
# read-only property fahrenheit that converts and returns the value derived from celsius.
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    @property
    def celsius(self):
        return self.__celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.__celsius = value
    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32
t = Temperature(25)
print(t.celsius)
print(t.fahrenheit)
try:
    t.celsius = -300
except ValueError as e:
    print(f"ValueError: {e}")