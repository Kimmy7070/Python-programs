def avg(*n):
    avg=0
    c=0
    for i in n:
        avg+=int(i)
        c+=1
    avg/=c
    return avg
n=input("Enter the numbers ")
a=n.split()
print("The average is ",avg(*a))