#General Elections

from random import randint

import time

votes1 = (randint(1, 30000))
votes2 = (randint(1, 30000))
votes3 = (randint(1, 30000))
votes4 = (randint(1, 30000))

print("Presidential Election 2016")
print("\n")
time.sleep(1)
print("Candidates: ")
print("\n")
print("1.Barack Obama")
print("2.David Cameron")
print("3.Donald Trump")
print("4.Hilary Clinton")
print("\n")

president = input("Candidate: ")
president = president.lower()

#Barack Obama
if president == ("barack obama") or president == ("obama") or president == ("barack") or president == ("1"):
    print("You chose: Barack Obama")
    print("\n")
#Checks if you want to continue
    obamacheck = input("Do you wish to continue? Y/N: ")
    obamacheck = obamacheck.lower()
    #checks if the user has entered yes or y
    if obamacheck == ("y") or obamacheck == ("yes"):
        print("Vote processed.")
        print("Barack Obama's current votes: ", + votes1+1)
        time.sleep(1)
        print("\n")
        print("General Election 2016 Finished!")
        print("\n")
        print("Here are the candidates with their votes: ")
        print("Barack Obama: ", + votes1+1)
        print("David Cameron: ", + votes2)
        print("Donald Trump: ", + votes3)
        print("Hilary Clinton: ", + votes4)
    else:
        print("Vote cancelled.")

#David Cameron
elif president == ("david cameron") or president == ("cameron") or president == ("david") or president == ("2"):
    print("You chose: David Cameron")
    print("\n")
#Checks if you want to continue
    davidcheck = input("Do you wish to continue? Y/N: ")
    davidcheck = davidcheck.lower()
    #checks if the user has entered yes or y
    if davidcheck == ("y") or davidcheck == ("yes"):
        print("Vote processed.")
        print("David Cameron's current votes: ", + votes2+1)
        time.sleep(1)
        print("\n")
        print("General Election 2016 Finished!")
        print("\n")
        print("Here are the candidates with their votes: ")
        print("Barack Obama: ", + votes1)
        print("David Cameron: ", + votes2+1)
        print("Donald Trump: ", + votes3)
        print("Hilary Clinton: ", + votes4)
    else:
        print("Vote cancelled.")

#Donald Trump
elif president == ("donald trump") or president == ("trump") or president == ("donald") or president == ("3"):
    print("You chose: Donald Trump")
    print("\n")
#Checks if you wish to continue
    trumpcheck = input("Do you wish to continue? Y/N: ")
    trumpcheck = trumpcheck.lower()
    #checks if the user has entered yes or y
    if trumpcheck == ("y") or trumpcheck == ("yes"):
        print("Vote processed.")
        print("Donald Trump's current votes: ", + votes3+1)
        time.sleep(1)
        print("\n")
        print("General Election 2016 Finished!")
        print("\n")
        print("Here are the candidates with their votes: ")
        print("Barack Obama: ", + votes1)
        print("David Cameron: ", + votes2)
        print("Donald Trump: ", + votes3+1)
        print("Hilary Clinton: ", + votes4)
    else:
        print("Vote cancelled.")

#Hilary Clinton
elif president == ("hilary clinton") or president == ("clinton") or president == ("hilary") or president == ("4"):
    print("You chose: Hilary Clinton")
    print("\n")
#Checks if you wish to continue
    hilarycheck = input("Do you wish to continue? Y/N: ")
    hilarycheck = hilarycheck.lower()
    #checks if the user has entered yes or y
    if hilarycheck == ("y") or hilarycheck == ("yes"):
        print("Vote processed.")
        print("Hilary Clinton's current votes: ", + votes4+1)
        time.sleep(1)
        print("\n")
        print("General Election 2016 Finished!")
        print("\n")
        print("Here are the candidates with their votes: ")
        print("Barack Obama: ", + votes1)
        print("David Cameron: ", + votes2)
        print("Donald Trump: ", + votes3)
        print("Hilary Clinton: ", + votes4+1)
    else:
        print("Vote cancelled.")
#if candidate doesn't exist print this
else:
    print("Please enter a valid candidate.")