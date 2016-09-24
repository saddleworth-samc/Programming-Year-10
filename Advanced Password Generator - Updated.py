#Advanced Password Generator - SecuroKey
#Sam Gibson
#Connor Howarth
#24/09/2016

import random
import os
import time

#Add to clipboard


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

#Simple Passwords
SimpleLower1 = random.choice("abcdefghijklmnopqrstuvwxyz")
SimpleHigher1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
SimpleNumber1 = random.choice("1234567890")
SimpleSymbol1 = random.choice("!£$%^&*")
SimpleHigher2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
SimpleLower2 = random.choice("abcdefghijklmnopqrstuvwxyz")
SimpleNumber2 = random.choice("1234567890")
SimpleSymbol2 = random.choice("!£$%^&*")


#Standard Passwords
StandardLower1 = random.choice("abcdefghijklmnopqrstuvwxyz")
StandardHigher1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
StandardNumber1 = random.choice("1234567890")
StandardSymbol1 = random.choice("!£$%_+=^&*")
StandardHigher2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
StandardLower2 = random.choice("abcdefghijklmnopqrstuvwxyz")
StandardNumber2 = random.choice("1234567890")
StandardSymbol2 = random.choice("!£$%_+=^&*")
StandardHigher3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
StandardNumber3 = random.choice("1234567890")


#Hard Passwords
HardLower1 = random.choice("abcdefghijklmnopqrstuvwxyz")
HardLower2 = random.choice("abcdefghijklmnopqrstuvwxyz")
HardLower3 = random.choice("abcdefghijklmnopqrstuvwxyz")
HardLower4 = random.choice("abcdefghijklmnopqrstuvwxyz")
HardNumber1 = random.choice("1234567890")
HardNumber2 = random.choice("1234567890")
HardNumber3 = random.choice("1234567890")
HardNumber4 = random.choice("1234567890")
HardSymbol1 = random.choice("!£$%_+=^&*<>")
HardSymbol2 = random.choice("!£$%_+=^&*<>")
HardSymbol3 = random.choice("!£$%_+=^&*<>")
HardSymbol4 = random.choice("!£$%_+=^&*<>")
HardHigher1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
HardHigher2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
HardHigher3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
HardHigher4 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#Complex Passwords
ComplexLower1 = random.choice("abcdefghijklmnopqrstuvwxyz")
ComplexLower2 = random.choice("abcdefghijklmnopqrstuvwxyz")
ComplexLower3 = random.choice("abcdefghijklmnopqrstuvwxyz")
ComplexLower4 = random.choice("abcdefghijklmnopqrstuvwxyz")
ComplexLower5 = random.choice("abcdefghijklmnopqrstuvwxyz")
ComplexSymbol1 = random.choice("!£$%_+=^&*<>«»")
ComplexSymbol2 = random.choice("!£$%_+=^&*<>«»")
ComplexSymbol3 = random.choice("!£$%_+=^&*<>«»")
ComplexSymbol4 = random.choice("!£$%_+=^&*<>«»")
ComplexSymbol5 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}")
ComplexHigher1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ComplexHigher2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ComplexHigher3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ComplexHigher4 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ComplexHigher5 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ComplexNumber1 = random.choice("1234567890")
ComplexNumber2 = random.choice("1234567890")
ComplexNumber3 = random.choice("1234567890")
ComplexNumber4 = random.choice("1234567890")
ComplexNumber5 = random.choice("1234567890")


#UnCrackable Passwords'
UnCrackableLower1 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower2 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower3 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower4 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower5 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower6 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableLower7 = random.choice("abcdefghijklmnopqrstuvwxyz")
UnCrackableHigher1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher4 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher5 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher6 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableHigher7 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
UnCrackableSymbol1 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol2 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol3 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol4 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol5 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol6 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableSymbol7 = random.choice("!£$%_+=^&*<>«»/\|'@#~`¬[]{}-")
UnCrackableNumber1 = random.choice("1234567890")
UnCrackableNumber2 = random.choice("1234567890")
UnCrackableNumber3 = random.choice("1234567890")
UnCrackableNumber4 = random.choice("1234567890")
UnCrackableNumber5 = random.choice("1234567890")
UnCrackableNumber6 = random.choice("1234567890")
UnCrackableNumber7 = random.choice("1234567890")

#What happens on startup
print("Welcome to SecuroKey!")
time.sleep(3)
print("\n")
print ("Password Complexity: ")
time.sleep(1)
print ("\n")
print ("Simple")
print ("Standard")
print ("Hard")
print ("Complex")
print ("Un-Crackable")
print ("\n")
time.sleep(1)


#Simple Password Print
complexity = input("Enter Complexity: ")
if complexity == ("Simple") or complexity == ("simple"):
    addToClipBoard(SimpleLower1 + SimpleHigher1 + SimpleSymbol1 + SimpleNumber1 + SimpleHigher2 + SimpleLower2 + SimpleSymbol2 + SimpleNumber2)
    print(SimpleLower1 + SimpleHigher1 + SimpleSymbol1 + SimpleNumber1 + SimpleHigher2 + SimpleLower2 + SimpleSymbol2 + SimpleNumber2)
    print("\n")
    print("Thank-you for using SecuroKey!")



#Standard Password Print
elif complexity == ("Standard") or complexity == ("standard"):
    addToClipBoard(StandardNumber3 + StandardHigher3 + StandardSymbol2 + StandardNumber2 + StandardHigher2 + StandardLower2 + StandardSymbol1 + StandardNumber1 + StandardHigher1 + StandardLower1)
    print(StandardNumber3 + StandardHigher3 + StandardSymbol2 + StandardNumber2 + StandardHigher2 + StandardLower2 + StandardSymbol1 + StandardNumber1 + StandardHigher1 + StandardLower1)
    print("\n")
    print("Thank-you for using SecuroKey!")



#Hard Password Print
elif complexity == ("Hard") or complexity == ("hard"):
    addToClipBoard(HardNumber1 + HardHigher1 + HardLower1 + HardSymbol1 + HardNumber2 + HardHigher2 + HardLower2 + HardSymbol2 + HardNumber3 + HardHigher3 + HardLower3 + HardSymbol3 + HardNumber4 + HardHigher4 + HardLower4 + HardSymbol4)
    print(HardNumber1 + HardHigher1 + HardLower1 + HardSymbol1 + HardNumber2 + HardHigher2 + HardLower2 + HardSymbol2 + HardNumber3 + HardHigher3 + HardLower3 + HardSymbol3 + HardNumber4 + HardHigher4 + HardLower4 + HardSymbol4)
    print("\n")
    print("Thank-you for using SecuroKey!")



#Complex Password Print
elif complexity == ("Complex") or complexity == ("complex"):
    addToClipBoard(ComplexLower1 + ComplexHigher1 + ComplexSymbol1 + ComplexNumber1 + ComplexLower2 + ComplexHigher2 + ComplexSymbol2 + ComplexNumber2 + ComplexLower3 + ComplexHigher3 + ComplexSymbol3 + ComplexNumber3 + ComplexLower4 + ComplexHigher4 + ComplexSymbol4 + ComplexNumber4 + ComplexLower5 + ComplexHigher5 + ComplexSymbol5 + ComplexNumber5)
    print(ComplexLower1 + ComplexHigher1 + ComplexSymbol1 + ComplexNumber1 + ComplexLower2 + ComplexHigher2 + ComplexSymbol2 + ComplexNumber2 + ComplexLower3 + ComplexHigher3 + ComplexSymbol3 + ComplexNumber3 + ComplexLower4 + ComplexHigher4 + ComplexSymbol4 + ComplexNumber4 + ComplexLower5 + ComplexHigher5 + ComplexSymbol5 + ComplexNumber5)
    print("\n")
    print("Thank-you for using SecuroKey!")



#UnCrackable Password Print
elif complexity == ("Un-Crackable") or complexity == ("UnCrackable") or complexity == ("uncrackable") or complexity == ("un-crackable"):
    addToClipBoard(UnCrackableLower1 + UnCrackableHigher1 + UnCrackableSymbol1 + UnCrackableNumber1 + UnCrackableLower2 + UnCrackableHigher2 + UnCrackableSymbol2 + UnCrackableNumber2 + UnCrackableLower3 + UnCrackableHigher3 + UnCrackableSymbol3 + UnCrackableNumber3 + UnCrackableLower4 + UnCrackableHigher4 + UnCrackableSymbol4 + UnCrackableNumber4 + UnCrackableLower5 + UnCrackableHigher5 + UnCrackableSymbol5 + UnCrackableNumber5 + UnCrackableLower6 + UnCrackableHigher6 + UnCrackableSymbol6 + UnCrackableNumber6 + UnCrackableLower7 + UnCrackableHigher7 + UnCrackableSymbol7 + UnCrackableNumber7)
    print(UnCrackableLower1 + UnCrackableHigher1 + UnCrackableSymbol1 + UnCrackableNumber1 + UnCrackableLower2 + UnCrackableHigher2 + UnCrackableSymbol2 + UnCrackableNumber2 + UnCrackableLower3 + UnCrackableHigher3 + UnCrackableSymbol3 + UnCrackableNumber3 + UnCrackableLower4 + UnCrackableHigher4 + UnCrackableSymbol4 + UnCrackableNumber4 + UnCrackableLower5 + UnCrackableHigher5 + UnCrackableSymbol5 + UnCrackableNumber5 + UnCrackableLower6 + UnCrackableHigher6 + UnCrackableSymbol6 + UnCrackableNumber6 + UnCrackableLower7 + UnCrackableHigher7 + UnCrackableSymbol7 + UnCrackableNumber7)
    print("\n")
    print("Thank-you for using SecuroKey!")
#What happens if user enters a wrong type
else:
    print("Invalid password type.")