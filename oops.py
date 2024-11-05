

# OOP concepts in Python:


#  Encapsulation
# Encapsulation restricts access to certain components. You use private attributes (by convention, prefixing with _ or __) that should not be directly accessed outside the class.
# Getters and Setters can be used to access private attributes.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500


# Inheritance
# Inheritance allows one class (the child or derived class) to inherit attributes and methods from another class (the parent or base class).
# This helps reuse code and create a hierarchy of classes.

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound())  # Output: "Woof!"

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass. For example, a Dog and Cat class both inherit from Animal but have their own sound method.

class Cat(Animal):
    def sound(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())  # Output: "Woof!", "Meow!"

# Abstraction
# Abstraction means creating classes that represent abstract concepts and do not have direct instances. Abstract classes often serve as templates for derived classes.
# In Python, you can use the abc module to define abstract classes and methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())  # Output: 12

# Dunder (Magic) Methods
# Dunder methods (like __init__, __str__, __len__, etc.) are special methods that allow objects to interact with Python’s built-in functions.
# For example, __str__ lets you customize what’s displayed when print() is called on an object.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("1984", "George Orwell")
print(book)  # Output: "1984 by George Orwell"

