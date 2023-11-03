# Coding for Noncoders: Object-Oriented Programming (OOP)

## Introduction

In this beginner-friendly hands-on lab, you will learn about Object-Oriented Programming (OOP) concepts in Python. OOP is a fundamental programming paradigm used to create reusable and organized code. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `oop_basics.py`.

### Step 3: Introduction to Classes and Objects

In Python, classes are used to define objects, which are instances of those classes. Let's explore how to create classes and objects.

1. **Creating a Simple Class:**

   - Define a class named `Person`.
   - Inside the class, create an `__init__` method that takes two parameters, `name` and `age`.
   - Inside the `__init__` method, initialize instance variables `self.name` and `self.age` with the provided values.

   ```python
   # Creating a Simple Class
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   ```

2. **Creating Objects (Instances):**

   - Create two instances of the `Person` class with different names and ages.
   - Print the attributes of each person.

   ```python
   # Creating Objects (Instances)
   person1 = Person("Alice", 30)
   person2 = Person("Bob", 25)

   print("Person 1: Name =", person1.name, ", Age =", person1.age)
   print("Person 2: Name =", person2.name, ", Age =", person2.age)
   ```

### Step 4: Class Methods

In Python, classes can have methods, which are functions defined inside the class. Let's explore how to add methods to a class.

1. **Adding a Method to the Class:**

   - Add a method named `greet` to the `Person` class.
   - The `greet` method should print a greeting message using the `name` attribute.

   ```python
   # Adding a Method to the Class
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def greet(self):
           print(f"Hello, my name is {self.name} and I am {self.age} years old.")
   ```

2. **Calling the Class Method:**

   - Create a new instance of the `Person` class.
   - Call the `greet` method for the person.

   ```python
   # Calling the Class Method
   person3 = Person("Charlie", 28)
   person3.greet()
   ```

### Step 5: Conclusion

In this hands-on lab, you learned the basics of Object-Oriented Programming (OOP) in Python. Classes are used to define blueprints for creating objects, and objects are instances of those classes. Methods in classes allow you to define behaviors associated with objects.

To explore more about classes and objects in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/classes.html). The documentation provides detailed information and examples on using classes and objects.

Happy coding!
