n=int(input("Enter a number"))
f=0
for i in range (2,n//2+1):
    if n%i==0:
        f+=1
        break
if f==0:
    print("Prime number")
else:
    print("Not prime number")