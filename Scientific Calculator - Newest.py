#Scientific Calculator
#Sam Gibson
#Connor Howarth
#24/09/2016 (started)
#Ongoing development.

#Changelog
#Added: calculator = calculator.lower(), this means you can enter any variable. For example "add", "aDD"
#Removed: long elif lines.

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


def pathag(sidea, sideb):
    csquare = (sidea ** 2) + (sideb ** 2)
    sidec = math.sqrt(csquare)
    return sidec


print("Scientific Calculator.")
time.sleep(1)
print("\n")
print("Types:")
time.sleep(1)
print("\n")
print("1.Add")
print("2.Divide")
print("3.Powers")
print("4.Factors")
print("5.Subtract")
print("6.Multiply")
print("7.Remainder")
print("8.Percentage")
print("9.Square Root")
print("10.Square (Area)")
print("11.Circle (Area)")
print("12.Rectangle (Area)")
print("13.Times Tables (1-10)")
print("14.Pythagoras' Theorem")
time.sleep(1)
print("\n")

calculator = input("Enter the type: ")
#ADD = 1
calculator = calculator.lower()
if calculator == ("add") or calculator == ("+") or calculator == ("1"):
    print("\n")
    print("Type set to: Add.")
    print("\n")
    number1add = int(input("Enter the first number.:"))
    number2add = int(input("Enter the second number: "))
    print("Answer = ", + number1add + number2add)
#MINUS = 5
    print("\n")
elif calculator == ("-") or calculator == ("minus") or calculator == ("5"):
    print("Type set to: Subtract.")
    print("\n")
    number1take = int(input("Enter the first number: "))
    number2take = int(input("Enter the second number: "))
    print("Answer = ", + number1take - number2take)
#DIVIDE = 2
elif calculator == ("/") or calculator == ("divide") or calculator == ("subtract") or calculator == ("2"):
    print("\n")
    print ("Type set to: Divide.")
    print("\n")
    number1divide = int(input("Enter the first number: "))
    number2divide = int(input("Enter the second number: "))
    print("Answer = ", + number1divide / number2divide)
#MULTIPLY = 6
elif calculator == ("*") or calculator == ("times") or calculator == ("multiply") or calculator == ("6"):
    print("\n")
    print("Type set to: Multiplication.")
    print("\n")
    number1times = int(input("Enter the first number: "))
    number2times = int(input("Enter the second number: "))
    print("Answer = ", + number1times * number2times)
#Powers = 3
elif calculator == ("**") or calculator == ("powers") or calculator == ("power") or calculator == ("3"):
    print("\n")
    print("Type set to: Powers.")
    print("\n")
    number1power = int(input("Enter the first number: "))
    number2power = int(input("To the power of: "))
    print("Answer = ", + number1power ** number2power)
#Square Root = 9
elif calculator == ("square root") or calculator == ("squareroot") or calculator == ("9"):
    print("\n")
    print("Type set to: Square Root")
    print("\n")
    number1root = int(input("Enter a number: "))
    print("Answer = ", + number1root ** 0.5)
#Percentage = 8
elif calculator == ("percentage") or calculator == ("percent") or calculator == ("8"):
    print("\n")
    print("Type set to: Percentage")
    print("\n")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    percentage = num1 / num2 * 100
    print (num1 / num2 * 100, "%")
#Remainder = 7
elif calculator == ("remainder") or calculator == ("remainders") or calculator == ("7"):
    print("\n")
    print("Type set to: Remainder.")
    print("\n")
    number1times = int(input("Enter a number: "))
    number2times = int(input("Divided by: "))
    print("Remainder = ", + number1times % number2times)
#Factors = 4
elif calculator == ("factors") or calculator == ("factor") or calculator == ("4"):
    print("\n")
    print("Type set to: Factors")
    print("\n")
    numfactor1 = int(input("Enter the number: "))
    print("The factors of", numfactor1, "are:")
    for i in range(1, numfactor1 + 1):
        if numfactor1 % i == 0:
            print(i)
#Circle (Area) = 11
elif calculator == ("circle") or calculator == ("11"):
    print("\n")
    print("Type set to: Circle (Area)")
    print("\n")
    radius = float(input("Enter the radius of the circle: "))
    area = circleArea(radius, pi)
    print("The area is: ", str(area))
#Rectangle (Area) = 12
elif calculator == ("rectangle") or calculator == ("12"):
    print("\n")
    print("Type set to: Rectangle (Area)")
    print("\n")
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = areaRectangle(height, width)
    print("The area is: ", str(area))
#Square (Area) = 10
elif calculator == ("square") or calculator == ("10"):
    print("\n")
    print("Type set to: Square (Area)")
    print("\n")
    height = float(input("Enter the height of the square: "))
    width = float(input("Enter the width of the square: "))
    area = areaRectangle(height, width)
    print("The area is: ", str(area))
#Pythagoras' Theorem = 1
elif calculator == ("pythagoras theorem") or calculator == ("14"):
    print("\n")
    print("Type set to: Pythagoras' Theorem.")
    print("\n")
    a = float(input("Side A: "))
    b = float(input("Side B: "))
    numberpyth = pathag(a, b)
    print("Side C is", + numberpyth)
#Times Tables = 13
elif calculator == "times tables" or calculator == "time table" or calculator == "13":
    print("\n")
    print("Type set to: Times Table")
    print("\n")
    tables = input("Enter Times Table: ")
    #1 times table
    if tables == ("1"):
        for i in range(1, 11):
            ttValue1 = 1 * i
            print(ttValue1)
    #2 times table
    elif tables == ("2"):
        for i in range(1, 11):
            ttValue2 = 2 * i
            print(ttValue2)
    #3 times table
    elif tables == ("3"):
        for i in range(1, 11):
            ttValue2 = 3 * i
            print(ttValue2)
    #4 times table
    elif tables == ("4"):
        for i in range(1, 11):
            ttValue4 = 4 * i
            print(ttValue4)
    #5 times table
    elif tables == ("5"):
        for i in range(1, 11):
            ttValue5 = 5 * i
            print(ttValue5)
    #6 times table
    elif tables == ("6"):
        for i in range(1, 11):
            ttValue6 = 6 * i
            print(ttValue6)
    #7 times table
    elif tables == ("7"):
        for i in range(1, 11):
            ttValue7 = 7 * i
            print(ttValue7)
    #8 times table
    elif tables == ("8"):
        for i in range(1, 11):
            ttValue8 = 8 * i
            print(ttValue8)
    #9 times table
    elif tables == ("9"):
        for i in range(1, 11):
            ttValue9 = 9 * i
            print(ttValue9)
    #10 times table
    elif tables == ("10"):
        for i in range(1, 11):
            ttValue10 = 10 * i
            print(ttValue10)
    elif tables != ("10") or tables != ("9") or tables != ("8") or tables != ("7") or tables != ("6") or tables != ("5") or tables != ("4") or tables != ("3") or tables != ("2") or tables != ("1"):
#Needed to manually print "else" which is "!=". "else" gets mixed up with the "else" beneath.
            print("Please enter a valid integer between 1-10.")
else:
    print("Please enter a valid type.")
