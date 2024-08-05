# Q.1Write a program for arithmatic operators
# answer

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def arithmetic_operations(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

arithmetic_operations(a, b)

# Q.2 Write a program for assignment operators
# answer

x=10
def assignment_operations(x):
    print(f"Initial value of x: {x}")

    x += 5
    print(f"After x += 5: {x}")

    x -= 3
    print(f"After x -= 3: {x}")

    x *= 2
    print(f"After x *= 2: {x}")

    x /= 4
    print(f"After x /= 4: {x}")

    x //= 2
    print(f"After x //= 2: {x}")

    x %= 3
    print(f"After x %= 3: {x}")

    x **= 2
    print(f"After x **= 2: {x}")

assignment_operations(x)


# Q.3Write a program for Bitwise operators 
# answer
def bitwise_operations(a, b):
    print(f"Bitwise AND: {a} & {b} = {a & b}")
    print(f"Bitwise OR: {a} | {b} = {a | b}")
    print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
    print(f"Bitwise NOT: ~{a} = {~a}")
    print(f"Left Shift: {a} << 2 = {a << 2}")
    print(f"Right Shift: {a} >> 2 = {a >> 2}")

bitwise_operations(5, 3)


# Q.4 Write a program to calculate greatest of three numbers.
#answer


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
def greatest_of_three(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    print(f"The greatest of {a}, {b}, and {c} is {greatest}")


greatest_of_three(a, b, c)

# 1.Calculate the area of a circle.
#answer
import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    print(f"Area of the circle with radius {radius} is {area}")


area_of_circle(5)


# 2.Calculate the area of a triangle.
# answer
base=int(input("Enter the base: "))
height=int(input("Enter the second height: "))

def area_of_triangle(base, height):
    area = 0.5 * base * height
    print(f"Area of the triangle with base {base} and height {height} is {area}")


area_of_triangle(base, height)


# 3.Calculate the area of a rectangle.
# answer
l=int(input("Enter the length: "))
b=int(input("Enter the width: "))
def area_of_rectangle(length, width):
    area = length * width
    print(f"Area of the rectangle with length {length} and width {width} is {area}")


area_of_rectangle(l, b)


# 4.Calculate the area of a square
# answer
def area_of_square(side):
    area = side ** 2
    print(f"Area of the square with side {side} is {area}")


area_of_square(4)

