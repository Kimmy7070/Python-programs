def power (x,y):
    p=1
    for i in range (y):
        p*=x
    return(p)
x=int(input("Enter the base number"))
y=int(input("Enter the power"))
print("The result is ",power(x,y))