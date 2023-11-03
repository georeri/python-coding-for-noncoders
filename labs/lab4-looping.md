# Coding for Noncoders: Loops

## Introduction

In this beginner-friendly hands-on lab, you will explore the concepts of for and while loops in Python. Loops allow you to repeat tasks multiple times, making your code more efficient and dynamic. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `loops.py`.

### Step 3: Explore `for` Loops

In Python, `for` loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. Let's explore how to use `for` loops.

1. **Using a `for` Loop with a List:**

   - Create a list of numbers (e.g., `numbers = [1, 2, 3, 4, 5]`).
   - Use a `for` loop to iterate over the list and print each number.

   ```python
   # Using a for Loop with a List
   numbers = [1, 2, 3, 4, 5]

   for number in numbers:
       print(number)
   ```

2. **Using a `for` Loop with a String:**

   - Create a string (e.g., `text = "Hello"`).
   - Use a `for` loop to iterate over the string and print each character.

   ```python
   # Using a for Loop with a String
   text = "Hello"

   for char in text:
       print(char)
   ```

### Step 4: Explore `while` Loops

In Python, `while` loops are used to execute a block of code as long as a condition is `True`. Let's explore how to use `while` loops.

1. **Using a `while` Loop to Count:**

   - Create a variable `count` and set it to 1.
   - Use a `while` loop to print the value of `count` and increment it by 1 in each iteration.
   - Set a condition to stop the loop after a certain number of iterations (e.g., stop after `count` reaches 5).

   ```python
   # Using a while Loop to Count
   count = 1

   while count <= 5:
       print(count)
       count += 1
   ```

2. **Using a `while` Loop with User Input:**

   - Use a `while` loop to ask the user for input (e.g., their name).
   - Continue asking for input until the user enters "quit" (use the `input()` function).
   - Print a message when the loop exits.

   ```python
   # Using a while Loop with User Input
   user_input = ""

   while user_input != "quit":
       user_input = input("Enter your name (type 'quit' to exit): ")

   print("Goodbye!")
   ```

### Step 5: Conclusion

In this hands-on lab, you explored `for` and `while` loops in Python. Loops are powerful tools that allow you to perform repetitive tasks and control the flow of your programs. Understanding how to use loops is fundamental in programming.

To delve deeper into loops and iteration in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/controlflow.html#the-range-function). The documentation provides detailed information and examples on using loops and the `range()` function.

Happy coding!
