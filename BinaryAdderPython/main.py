#Main Module

#Necessary modules imported
import greetings
import numValidation
import decimalToBinary
import binaryAddition

greetings.beginningGreeting()

loop=True
#while loop that only terminates when the user desires
while loop==True:
    print("Enter first decimal number:")
    #Functions called for exception handling and number range validation for first number
    fnum=numValidation.errorCheck()
    fnum=numValidation.checkNum(fnum)
    print("\n")

    print("Enter second decimal number:")
    #Functions called for exception handling and number range validation for second number
    snum=numValidation.errorCheck()
    snum=numValidation.checkNum(snum)
    print("\n")

    #Functions called for decimal to binary conversion
    binaryFnum=decimalToBinary.convert(fnum)
    binarySnum=decimalToBinary.convert(snum)

    #Function called for binary addition
    binarySum=binaryAddition.add(binaryFnum,binarySnum)

    #Displays final output of binary addition
    print("The sum is",binarySum,"\n")
    
    continueLoop=input("Do you wish to continue?(Enter N if you do not want to continue.)").upper()
    print("\n")
    if continueLoop=="N":
        loop=False
    
greetings.endGreeting()
