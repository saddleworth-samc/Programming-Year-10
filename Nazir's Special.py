#Mr Nazirs drive thru
#Connor Howarth
#Sam Gibson
#Created: 07/10/16

sold = float(input("How many burgers have been sold this month? "))#Defines how many burgers you have sold
money = sold * 4.30#Multiplies how many sold by 4.30 (the price of the burger)
stock = float(input("How much money have you spent on stock this month? "))#Defines how much has been spent on stock
profit1 = money - stock#Money left after stock prices
rent = 2000#Cost of rent
profit2 = profit1 - rent #Money left after rent
if profit2 > sold:#profit2 is bigger than sold(>)
    print ("You have made: £", + profit2)#This prints how much profit has been made
elif profit2 < sold:#profit2 is smaller than sold(<)
    print("Warning!")#A warning message
    print("You have lost: £", + profit2)#This prints how much has been lost
else:#This is here so if an invalid variable is inputted it prints the code below
    print("")#This prints when the user has inputted an invalid variable

