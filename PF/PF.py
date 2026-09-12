# ========================================
# Programming Fundamentals in One Program
# ========================================

# ----- 1. Variables & Data Types -----
name = "Ali"              # string
age = 20                  # integer
height = 5.8              # float
is_student = True         # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student?", is_student)

# ----- 2. Input & Output -----
user_input = input("Enter your favorite number: ")
print("You entered:", user_input)

# ----- 3. Type Casting -----
num = int(user_input)
print("Square is:", num ** 2)

# ----- 4. Operators -----
x, y = 10, 3
print("Addition:", x + y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Power:", x ** y)
print("Modulus:", x % y)

# ----- 5. Conditional Statements -----
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# ----- 6. Loops -----
# For loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1

# ----- 7. Functions -----
def greet(name):
    return f"Hello, {name}!"

print(greet("Abdullah"))

def factorial(n):
    # ----- 12. Recursion -----
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# ----- 8. Lists -----
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits list:", fruits)
print("First fruit:", fruits[0])

# ----- 9. Tuples -----
coordinates = (10, 20)
print("Tuple:", coordinates)

# ----- 10. Dictionaries -----
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print("Student Info:", student)
print("Name from dict:", student["name"])

# ----- 11. String Manipulation -----
sentence = "Python is powerful"
print("Upper:", sentence.upper())
print("Word count:", len(sentence.split()))

# ----- 13. File Handling -----
# Writing to a file
with open("data.txt", "w") as f:
    f.write("This is a test.\n")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()
    print("File content:", content)

# ----- 14. Exception Handling -----
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Result is:", result)
finally:
    print("This block always runs.")

# ----- 15. Importing Modules -----
import math
import random

print("Square root of 16:", math.sqrt(16))
print("Random number between 1-100:", random.randint(1, 100))
