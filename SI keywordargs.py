def SI(ti,p):
    SI=0.065*p*ti
    return SI
a=int(input("Enter the amount "))
t=float(input("Enter the time in years "))
print("The Simple interest will be ",SI(p=a,ti=t))
