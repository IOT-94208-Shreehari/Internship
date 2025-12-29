# Example demonstrating:
# 1. Default parameters
# 2. Keyword arguments
# 3. Passing a function to another function


# ---------- 1. Default Parameter Values ----------
def greet(name, message="Hello"):
    print(message, name)


# ---------- 2. Keyword Arguments ----------
def student_info(name, age, course="Python"):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# ---------- 3. Function Passed to Another Function ----------
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def operate(func, x, y):
    return func(x, y)


# ---------- Main Program ----------
def main():
    print("=== Default Parameter Example ===")
    greet("Alice")
    greet("Bob", "Welcome")

    print("\n=== Keyword Argument Example ===")
    student_info(name="John", age=21)
    student_info(age=22, course="Data Science", name="Emma")

    print("\n=== Passing Function to Another Function ===")
    result1 = operate(add, 10, 5)
    result2 = operate(multiply, 10, 5)

    print("Addition:", result1)
    print("Multiplication:", result2)


# Run the main function
main()
