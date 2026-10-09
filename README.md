<div align="center">

# 🐍 Multi-Utility Toolkit

### A Python-Based Collection of Useful Utilities

**Developed with 💙 by Asti Sojitra**

</div>

---

## 🛠️ Multi-Utility Toolkit

A beginner-friendly Python **Multi-Utility Toolkit** that combines different useful utilities into one menu-driven application. This project demonstrates the practical use of Python built-in modules, functions, loops, conditional statements, user input, file handling, and custom packages.

The main purpose of this project is to provide multiple utilities through a single application, making it easier to perform date and time operations, mathematical calculations, random data generation, UUID generation, and file operations.

This project is designed for beginners who want to understand how Python modules and packages work in real-world applications.

---

## 📌 Features

### 🕒 Date and Time
The Date and Time module provides useful features for working with dates, times, and elapsed time.

- Display the current date and time.
- Calculate the difference between two dates
- Format dates into different readable formats.
- Measure elapsed time using a stopwatch.
- Create a countdown timer.
- Perform date calculations using the datetime module.
- Measure time intervals using the time module.


### 🧮 Mathematical Operations
The Mathematical Operations module performs common mathematical calculations using Python's built-in math module.

- Calculate the factorial of a number.
- Calculate compound interest.
- Calculate the area of a circle,rectangle and triangle.
- Calculate the natural logarithm of a number.
- Use mathematical constants and functions provided by Python.

### 🎲 Random Data Generation
The Random Data Generation module demonstrates how to generate random values using Python's random and string modules.

- Generate a random integer number.
- Generate a list containing five random integers.
- Create a random password using letters, digits, and selected special characters.
- Generate a six-digit numeric OTP.
- Explore random selection and number generation.

### 🆔 UUID Generation
The UUID module generates a universally unique identifier using Python's uuid module.

- Generate a unique UUID using `uuid.uuid4()`

### 📁 File Operations
The File Operations module uses a custom Python package named MyPackage.

- Create a new file.
- Write content into a file.
- Read content from a file.
- Append additional content to an existing file.
- Understand file handling through a separate module.
- Organize reusable functions into a custom package.


### 🔍 Module Exploration
The Module Exploration feature demonstrates Python's built-in dir() function.

- Explore attributes available in the math,random,datetime,time,uuid and string module.
- Learn how Python modules expose functions, constants, and other attributes.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To understand the practical use of Python's built-in modules.
- To learn how to divide a program into multiple functions.
- To implement a menu-driven application.
- To practice loops and conditional statements.
- To understand how to accept and process user input.
- To perform mathematical calculations using Python.
- To work with dates and time intervals.
- To generate random numbers, passwords, and OTPs.
- To understand UUID generation.
- To learn basic file handling operations.
- To create and import custom modules and packages.
- To explore module attributes using the `dir()` function.
- To improve logical thinking and problem-solving skills.


## 📂 Project Structure

```text
Moduler & Packager/
│
├── Moduler & Packager.py
├── README.md
├── example.txt
├── Output.png
│
└── MyPackage/
    ├── __init__.py
    ├── file_operations.py
    │
    └── __pycache__/
        ├── __init__.cpython-314.pyc
        └── file_operations.cpython-314.pyc
```
---

## 🐍 Python Modules Used

The project uses Python's built-in modules:

```python
from datetime import datetime
import time
import math
import random
import uuid
import string
```

### Custom Module

```python
from MyPackage import file_operations
```

No external Python packages are required.

---

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

```text
================================
Welcome to Multi-Utility Toolkit
================================

Choose an option:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate a Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

---

## 🕒 Datetime and Time Operations

Provides date and time utilities using the `datetime` and `time` modules.

### Operations

- Display current date and time
- Calculate difference between two dates
- Format dates
- Stopwatch
- Countdown timer

### Example

```text
Current Date and Time: 2026-10-07 21:15:30
Difference: 9 days
Elapsed Time: 4.52 seconds
Time's up!
```

---

## 🧮 Mathematical Operations

Provides common mathematical calculations using the `math` module.

### Operations

- Factorial
- Compound interest
- Sine, cosine and tangent
- Circle, rectangle and triangle area
- Natural logarithm

### Example

```text
Factorial: 120
Compound Interest: 1025
Sin: 0.7071067811865475
Circle Area: 78.53981633974483
Logarithm: 2.302585092994046
```

---

## 🎲 Random Data Generation

Uses the `random` and `string` modules to generate random data.

### Operations

- Random number
- Random list
- Random password
- Six-digit OTP

### Example

```text
Random Number: 57
Random List: [23, 87, 12, 65, 41]
Generated Password: A7@kP2#xQ9
Generated OTP: 483921
```

> **Note:** Password and OTP generation are for educational purposes. For real security applications, use Python's `secrets` module.

---

## 🆔 UUID Operations

Generates a unique identifier using:

```python
uuid.uuid4()
```

### Example

```text
Generated UUID: 550e8400-e29b-41d4-a716-446655440000
```

---

## 📁 File Operations

The project uses a custom package named `MyPackage`.

```python
from MyPackage import file_operations
```

### Operations

- Create a new file
- Write content
- Read file content
- Append content

---

## 🔍 Explore Module Attributes

The project demonstrates Python's built-in `dir()` function.

### Example

```python
dir(math)
```

### Supported Modules

- `math`
- `random`
- `datetime`
- `time`
- `uuid`
- `string`

---

# 🧠 Python Concepts Demonstrated

This project demonstrates:

- Functions
- `while` loops
- `if-elif-else`
- User input
- Type conversion
- Modules and packages
- File handling
- Standard library
- Date and time operations
- Mathematical calculations
- Random data generation
- UUID generation
- `dir()` function
- Menu-driven programming

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.14.6 | Main programming language used to develop the project |
| Visual Studio Code (VS Code) | Code editor used for writing and running Python code |
| Git | Version control for tracking code changes |
| GitHub | Hosting the project repository and managing source code |

## 📚 Python Modules and Packages Used

| Module / Package | Purpose |
|------------------|---------|
| `datetime` | Date and time operations |
| `time` | Stopwatch and countdown functionality |
| `math` | Mathematical calculations |
| `random` | Random number, list, password, and OTP generation |
| `uuid` | Unique identifier generation |
| `string` | Character sets for password generation |
| `MyPackage` | Custom package for file operations |
---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/astisojitra-blip/Moduler-Packager.git
```

### 2. Open the project folder

```bash
cd "Moduler & Packager"
```

### 3. Run the program

```bash
 python "Moduler & Packager.py"

```

---

# 🖥️ Sample Output

```text
================================
Welcome to Multi-Utility Toolkit
================================

Choose an option:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate a Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit

Enter your choice: 1

Current Date and Time: 2026-10-07 21:15:30
```

---

# 📄 License

This project is created for **educational purposes**.

You are free to modify and improve this project for your own learning and practice.

---

# ⭐ Conclusion

**Multi-Utility Toolkit** is a beginner-friendly Python project designed to practice multiple Python concepts in one application.

It provides hands-on experience with:

- Python standard library
- Functions and loops
- Modules and packages
- File handling
- Date and time operations
- Mathematical calculations
- Random data generation
- UUID generation
- User input
- Menu-driven programming