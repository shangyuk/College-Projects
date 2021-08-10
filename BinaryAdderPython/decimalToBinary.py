#Module for converting decimal number into binary number

#function that converts decimal number, received as parameter, to binary number and stores it in a list
def convert(num):
    #list variables declared/initialised
    bits=[]
    actualBinary=[]
    
    #for loop to create an 8-bit binary number from decimal number
    for i in range(8):
        remainder=num%2
        bits.append(remainder)
        num=num//2

    #for loop to reverse the "bits" list ,as the binary is stored in "bits" list is in reverse order
    for i in range(7,-1,-1):
        actualBinary.append(bits[i])

    return actualBinary
