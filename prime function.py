def prime(n):
    for i in range (2,n//2):
        if(n%i==0):
            return(False)
    return(True)
n=int(input("Enter the number "))
if(prime(n)):
    print("The number is prime")
else:
    print("The number is not prime")