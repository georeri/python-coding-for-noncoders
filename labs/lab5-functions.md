# Coding for Noncoders: Functions

## Introduction

In this beginner-friendly hands-on lab, you will learn how to define and use functions in Python. Functions allow you to make your code more modular by breaking it into smaller, reusable blocks. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `functions.py`.

### Step 3: Define and Use Functions

In Python, you can define a function using the `def` keyword. Functions can take inputs (parameters) and return outputs (values). Let's explore how to define and use functions.

1. **Defining and Using a Simple Function:**

   - Create a function called `greet` that takes one parameter, `name`, and prints a greeting message.
   - Call the `greet` function with your name as an argument.

   ```python
   # Defining and Using a Simple Function
   def greet(name):
       print(f"Hello, {name}!")

   greet("Alice")
   ```

2. **Function with a Return Value:**

   - Create a function called `add` that takes two parameters, `a` and `b`, and returns the sum of the two values.
   - Call the `add` function with two numbers as arguments and print the result.

   ```python
   # Function with a Return Value
   def add(a, b):
       result = a + b
       return result

   sum_result = add(3, 5)
   print(f"The sum is: {sum_result}")
   ```

3. **Function with Default Parameter Value:**

   - Create a function called `say_hello` that takes one parameter, `name`, with a default value of "Guest."
   - Call the `say_hello` function without providing an argument.
   - Call the `say_hello` function with your name as an argument.

   ```python
   # Function with Default Parameter Value
   def say_hello(name="Guest"):
       print(f"Hello, {name}!")

   say_hello()
   say_hello("Bob")
   ```

### Step 4: Function Modularity

Functions make your code more modular, allowing you to reuse blocks of code. In this step, you'll create a function that calculates the square of a number and use it multiple times.

- Create a function called `square` that takes one parameter, `number`, and returns the square of the number.
- Use the `square` function to calculate and print the square of numbers 1 to 5 in a loop.

```python
# Function Modularity
def square(number):
    return number ** 2

for num in range(1, 6):
    result = square(num)
    print(f"The square of {num} is {result}")
```

### Step 5: Conclusion

In this hands-on lab, you learned how to define and use functions in Python. Functions are essential for making your code more organized, modular, and reusable. They allow you to encapsulate blocks of code and perform specific tasks.

To explore more about functions in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions). The documentation provides detailed information and examples on defining and using functions.

Happy coding!
