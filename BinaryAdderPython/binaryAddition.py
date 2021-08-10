#Module for addition of two 8-bit binary numbers

#function for addition of two 8-bit binary numbers
def add(A,B):
    #declaration and initialization of variables storing the binary sum
    binarySum=[]
    actualBinarySum=""

    #declaration and initialization of carryIn number
    C=0
    
    #for loop for addition of the binary numbers
    for i in range(7,-1,-1):
        #calculation for sum of individual bits
        binarySum.append(A[i]^B[i]^C)
        
        #calculation for carry in/out bit
        C=(C&(A[i]^B[i]))|(A[i]&B[i])

    #if condition for when a binary sum exceeds 8-bit digits
    if C==1:
        actualBinarySum=actualBinarySum+str(C)
        x=1
        print("The sum exceeds 8-bit binary number.")
    else:
        x=0

    #for loop for reversing and storing the binary sum in correct order
    for i in range(7,-1,-1):
        #if condition for removing unnecessary 0s from the final sum
        if binarySum[i]==1 or x==1 or i==0:
            actualBinarySum=actualBinarySum+str(binarySum[i])
            if binarySum[i]==1:
                x=1

    return actualBinarySum
