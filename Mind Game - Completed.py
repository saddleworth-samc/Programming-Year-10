# Mind games
# Connor Howarth
# Sam Gibson


import time


name = input("What's your name? ")
time.sleep (2)#Waits 2 seconds
print("\n")
print ("So, " + name + ", let's play a game.")
print("\n")

endLoop = 0
while endLoop == 0:
    endCheck = input("In this game I'm going to read your mind. Type 'Yes' to continue. ")#Keeps asking for the answer "Yes"
    if endCheck == 'yes' or endCheck == 'Yes':
        endLoop = 1
print("\n")
print("Let's begin.")

time.sleep (1)#Waits 3 seconds
print("\n") #Print blank line)s
time.sleep(2)
age = int(input("So, " + name + " how old are you? "))
time.sleep (1)#Waits 3 seconds
print("\n") #Print blank line
time.sleep(1)
print("Add 3 to your age.")
time.sleep(1)
print("\n") #Print blank line
print("You should have: ")
age += 3
print(age)
time.sleep(3)
print("\n") #Print blank line
print("Remember that number.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print("\n") #Print blank line
print("Now take 5 from your number.")
print("\n")
time.sleep(1)
print("You should have:")
age -= 5
print(age)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print ("\n") #Print blank line
print("Now, add 7 to your number")
print("\n")
time.sleep(1)
print("You should have:")
age += 7
print(age)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print ("\n") #Print blank line
print("\n")
time.sleep(3)
newage = int(input("So, what did you say your age was again? "))
print("\n")
time.sleep(2)
print("Take your current number and subtract your age. ")
print("\n")
time.sleep(1)
print("You should have:")
age -= newage
print(age)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print("\n")
print("Now, add 5 to that number. ")
print("\n")
time.sleep(1)
print("You should have:")
age += 5
print(age)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print("\n")
print("Now, multiply by 2 ")
print("\n")
time.sleep(1)
print("You should have:")
age *= 2
print(age)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print("\n")
print ("Final step, add 1 to your number ")
print("\n")
time.sleep(1)
print("\n")
time.sleep(1)
print("Remember that number. ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(3)
print("\n")
print("Wait for it...")
print("\n")
time.sleep(2)
print("I'm about to guess what number you're now thinking of...")
print("\n")
print("\n")
print("\n")
time.sleep(3)
print(" 222222222222222         1111111")
print("2:::::::::::::::22      1::::::1")
print("2::::::222222:::::2    1:::::::1")
print("2222222     2:::::2    111:::::1")
print("            2:::::2      1:::::1")
print("            2:::::2      1:::::1")
print("         2222::::2       1:::::1")
print("    22222::::::22        1:::::l")
print("  22::::::::222          1:::::l")
print(" 2:::::22222             1:::::l")
print("2:::::2                  1:::::l")
print("2:::::2                  1:::::l")
print("2:::::2       222222  1111:::::1111")
print("2::::::2222222:::::2 1::::::::::::1")
print("2::::::::::::::::::2 1::::::::::::1")
print("22222222222222222222  1111111111111 ")