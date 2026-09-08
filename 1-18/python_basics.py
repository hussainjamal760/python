import json
import math
import os


def variables_demo():
    age = 25
    height = 5.9
    name = "Alice"
    is_student = True
    print(name, age, height, is_student)


def numbers_demo():
    num1 = 15
    num2 = 4
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    integer_division = num1 // num2
    modulus = num1 % num2
    power = num1**num2
    print(addition, subtraction, multiplication, division, integer_division, modulus, power)
    square_root = math.sqrt(64)
    print(square_root)


def strings_demo():
    greeting = "Hello"
    target = "World"
    full_text = greeting + " " + target
    print(full_text)
    formatted = f"{greeting}, {target}! Welcome to Python."
    print(formatted)
    text = "  python programming  "
    print(text.upper())
    print(text.lower())
    print(text.strip())
    print(text.replace("python", "awesome"))
    words = text.strip().split(" ")
    print(words)
    print(full_text[0:5])


def lists_demo():
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    print(fruits)
    print(fruits[0])
    fruits[1] = "mango"
    print(fruits)
    fruits.remove("cherry")
    popped_item = fruits.pop()
    print(fruits, popped_item)
    fruits.sort()
    print(fruits)
    print(len(fruits))


def tuples_and_dictionaries_demo():
    point = (10, 20, 30)
    print(point[0], point[1])

    student = {
        "name": "John",
        "age": 20,
        "courses": ["Math", "CompSci"]
    }
    print(student["name"])
    student["grade"] = "A"
    student["age"] = 21
    print(student)

    for key, value in student.items():
        print(f"{key}: {value}")


def if_statement_demo():
    marks = 85
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    else:
        print("Grade: F")

    age = 20
    has_id = True
    if age >= 18 and has_id:
        print("Entry granted")


def loops_demo():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num * 2)

    for i in range(1, 6):
        if i == 3:
            continue
        if i == 5:
            break
        print(f"Index: {i}")


def calculate_area(length, width=1):
    return length * width


def greet_user(name):
    message = f"Welcome, {name}!"
    return message


def functions_demo():
    area1 = calculate_area(5, 4)
    area2 = calculate_area(7)
    greeting = greet_user("Hussain")
    print(area1, area2)
    print(greeting)


def json_demo():
    data = {
        "title": "Python Basics",
        "videos": 15,
        "completed": True
    }
    json_string = json.dumps(data)
    print(json_string)

    parsed_data = json.loads(json_string)
    print(parsed_data["title"])


def file_handling_demo():
    file_path = "sample.txt"
    with open(file_path, "w") as file:
        file.write("Hello, this is a line in the file.\n")
        file.write("Python file handling demonstration.\n")

    with open(file_path, "r") as file:
        content = file.read()
        print(content)

    if os.path.exists(file_path):
        os.remove(file_path)


def exception_handling_demo():
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    try:
        number = int("invalid_number")
        print(number)
    except ValueError:
        print("Invalid integer conversion.")
    finally:
        print("Execution completed.")


if __name__ == "__main__":
    variables_demo()
    numbers_demo()
    strings_demo()
    lists_demo()
    tuples_and_dictionaries_demo()
    if_statement_demo()
    loops_demo()
    functions_demo()
    json_demo()
    file_handling_demo()
    exception_handling_demo()
