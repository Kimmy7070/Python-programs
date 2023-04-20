n=int(input("Enter the limit"))
for i in range (1,n):
    for j in range (1,n+1-i):
        print(end=" ")
    for k in range (n,n-i,-1):
        print(k,end="")
    for l in range (n-i+2,n+1):
        print(l,end="")
    print()
for i in range (1,n+1):
    for j in range (1,i):
        print(end=" ")
    for k in range (n,i-1,-1):
        print(k,end="")
    for l in range (i+1,n+1):
        print(l,end="")
    print()
