from array import *
def avg_array(a):
    avg=0
    n=len(a)
    for i in range(n):
        avg+=a[i]
    avg/=n
    return avg
n=int(input("How many number's average?"))
a1=array('i',[])
print("Enter the array")
for i in range (n):
    a1.append(int(input()))
print("The average is ",avg_array(a1))
