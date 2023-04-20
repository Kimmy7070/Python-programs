def GCD(x,y,i):
    if i>0:
        if x%i==0 and y%i==0:
            return i
        else:
            return GCD(x,y,i-1)
    else:
        return 0
n1=int(input("Enter first number "))
n2=int(input("Enter the second number "))
if n1>n2:
    g=GCD(n1,n2,n2)
else:
    g=GCD(n1,n2,n1)
if g!=0:
    print("The GCD of the number is ",g)
else:
    print("No GCD found")
