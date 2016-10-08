#Mr Nazirs drive thru



sold = float(input("How many burgers have been sold this month?"))#Defines how many burgers you have sold
money = sold * 4.30#Multiplies how many sold by 4.30 (the price of the burger)
stock = float(input("How much money have you spent on stock this month?"))#Defines how much has been spent on stock
profit1 = money - stock#Money left after stock prices
rent = 2000#Cost of rent
profit2 = profit1 - rent #Money left after rent
if profit2 > sold:
    print ("You have made: £", + profit2)
else:
    print("")