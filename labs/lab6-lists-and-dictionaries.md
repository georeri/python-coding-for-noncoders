# Coding for Noncoders: Lists and Dictionaries

## Introduction

In this beginner-friendly hands-on lab, you will learn about data structures in Python, specifically lists and dictionaries. You will explore how to create, manipulate, and access data stored in these structures. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `data_structures.py`.

### Step 3: Explore Lists

In Python, a list is an ordered collection of items. Let's explore how to work with lists.

1. **Creating and Accessing Lists:**

   - Create a list of fruits (e.g., `fruits = ["apple", "banana", "cherry"]`).
   - Access and print the first item in the list.

   ```python
   # Creating and Accessing Lists
   fruits = ["apple", "banana", "cherry"]

   first_fruit = fruits[0]
   print("First fruit:", first_fruit)
   ```

2. **Modifying Lists:**

   - Add an item to the end of the list using the `append()` method.
   - Remove an item from the list using the `remove()` method.
   - Print the modified list.

   ```python
   # Modifying Lists
   fruits.append("orange")
   fruits.remove("banana")

   print("Updated list:", fruits)
   ```

### Step 4: Explore Dictionaries

In Python, a dictionary is an unordered collection of key-value pairs. Let's explore how to work with dictionaries.

1. **Creating and Accessing Dictionaries:**

   - Create a dictionary of contact information for a person (e.g., `contact_info = {"name": "Alice", "email": "alice@email.com", "phone": "123-456-7890"}`).
   - Access and print the person's name and email.

   ```python
   # Creating and Accessing Dictionaries
   contact_info = {"name": "Alice", "email": "alice@email.com", "phone": "123-456-7890"}

   person_name = contact_info["name"]
   person_email = contact_info["email"]

   print("Name:", person_name)
   print("Email:", person_email)
   ```

2. **Modifying Dictionaries:**

   - Add a new key-value pair to the dictionary.
   - Update an existing value.
   - Print the modified dictionary.

   ```python
   # Modifying Dictionaries
   contact_info["address"] = "123 Main St"
   contact_info["email"] = "new_email@email.com"

   print("Updated contact info:", contact_info)
   ```

### Step 5: Conclusion

In this hands-on lab, you learned about data structures in Python, specifically lists and dictionaries. Lists are used to store ordered collections of items, while dictionaries are used to store key-value pairs. These data structures are versatile and allow you to work with various types of data.

To explore more about lists and dictionaries in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/introduction.html#lists) for lists and [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). The documentation provides detailed information and examples.

Happy coding!
