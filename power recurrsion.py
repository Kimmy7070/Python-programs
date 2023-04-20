def power(x,y):
    if(y>0):
        return x*power(x,y-1)
    else:
        return 1
x=int(input("Enter the base "))
y=int(input("Enter the power "))
print("The answer is ",power(x,y))