#Scientific Calculator
#Sam Gibson
#Connor Howarth
#24/09/2016

import time
import math

pi = math.pi


def circleArea(radius, pi):
    #area of a circle is pi (3.14)
    #times square of radius
    area = pi * (radius * radius)
    return area


def areaRectangle(height, width):
    #area of a rectangle = height * width
    area = height * width
    return area

print("Scientific Calculator.")
time.sleep(1)
print("\n")
print("Types:")
time.sleep(1)
print("\n")
print("1.Add")
print("2.Divide")
print("3.Subtract")
print("4.Multiply")
print("5.Percentage")
print("6.Square Root")
print("7.Square (Area)")
print("8.Circle (Area)")
print("9.Rectangle (Area)")
time.sleep(1)
print("\n")

calculator = input("Enter the type: ")
#ADD
if calculator == ("+") or calculator == ("Add") or calculator == ("add") or calculator == ("1"):
    print("\n")
    print("Type set to: Add.")
    print("\n")
    number1add = int(input("Enter the first number. "))
    number2add = int(input("Enter the second number. "))
    print("Answer = ", + number1add + number2add)
#MINUS
    print("\n")
elif calculator == ("-") or calculator == ("minus") or calculator == ("Minus") or calculator == ("Subtract") or calculator == ("subtract") or calculator == ("3"):
    print("Type set to: Subtract.")
    print("\n")
    number1take = int(input("Enter the first number. "))
    number2take = int(input("Enter the second number. "))
    print("Answer = ", + number1take - number2take)
#DIVIDE
elif calculator == ("/") or calculator == ("Divide") or calculator == ("divide") or calculator == ("2"):
    print("\n")
    print ("Type set to: Divide.")
    print("\n")
    number1divide = int(input("Enter the first number. "))
    number2divide = int(input("Enter the second number. "))
    print("Answer = ", + number1divide / number2divide)
#TIMES
elif calculator == ("*") or calculator == ("Times") or calculator == ("times") or calculator == ("Multiply") or calculator == ("multiply") or calculator == ("4"):
    print("\n")
    print("Type set to: Multiplication.")
    print("\n")
    number1times = int(input("Enter the first number. "))
    number2times = int(input("Enter the second number. "))
    print("Answer = ", + number1times * number2times)
#Square Root
elif calculator == ("Square Root") or calculator == ("square root") or calculator == ("squareroot") or calculator == ("SquareRoot") or calculator == ("6"):
    print("\n")
    print("Type set to: Square Root")
    print("\n")
    number1root = int(input("Enter a number. "))
    print("Answer = ", + number1root ** 0.5)
#Percentage
elif calculator == ("Percentage") or calculator == ("percentage") or calculator == ("percent") or calculator == ("Percent") or calculator == ("5"):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    percentage = num1 / num2 * 100
    print (num1 / num2 * 100, "%")
#Circle
elif calculator == "Circle" or calculator == "circle" or calculator == ("8"):
    print("\n")
    print("Type set to: Circle (Area)")
    print("\n")
    radius = float(input("Enter the radius of the circle: "))
    area = circleArea(radius, pi)
    print("The area is: ", str(area))
#Rectangle
elif calculator == "Rectangle" or calculator == "rectangle" or calculator == ("9"):
    print("\n")
    print("Type set to: Rectangle (Area)")
    print("\n")
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = areaRectangle(height, width)
    print("The area is: ", str(area))
#Square
elif calculator == "Square" or calculator == "square" or calculator == ("7"):
    print("\n")
    print("Type set to: Square (Area)")
    print("\n")
    height = float(input("Enter the height of the square: "))
    width = float(input("Enter the width of the square: "))
    area = areaRectangle(height, width)
    print("The area is: ", str(area))
else:
    print("Please enter a valid type.")


