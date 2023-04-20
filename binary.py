def binary (n):
    if(n>1):
        if(n%2==0):
            return str(binary(n//2))+"0"
        else:
            return str(binary(n//2))+"1"
    else:
        return 1
n=int(input("Enter the number"))
print("The binary value of the number is ",binary(n))
