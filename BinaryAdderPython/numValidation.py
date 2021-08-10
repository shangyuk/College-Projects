#Module for exception handling and number range check

#function for taking input from user while exception handling
def errorCheck():
    valid=False
    #while loop that only terminates when no exception is called
    while valid==False:
        try:
            inpNum=int(input())
            valid=True
        except:
            print("\nInvalid Input! \n")
            print("Please, re-enter a decimal number between 0 and 255:")
                           
    return inpNum

#function to check whether the decimal number given by the user lies within the range of 0-255
def checkNum(num):
    #while loop that only terminates when a valid number in range is entered
    while num>255 or num<0:
        print("\nInvalid Input! \n")
        print("Please, re-enter a decimal number between 0 and 255:")
        num=errorCheck()#exception check and handling for re-entered number
            
    return num
