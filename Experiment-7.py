# Calculator using Pair Programming

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Error: Division by zero"

    return a / b


# Main Program

num1 = 20
num2 = 10

print("First Number:", num1)

print("Second Number:", num2)

print("Addition:", add(num1, num2))

print("Subtraction:", subtract(num1, num2))

print("Multiplication:", multiply(num1, num2))

print("Division:", divide(num1, num2))
