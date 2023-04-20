n=int(input("Enter the limit"))
for i in range (1,n):
    for j in range (1,n+1-i):
        print(end=" ")
    for k in range (1,i+1):
        print (k,end="")
    for l in range (i-1,0,-1):
        print (l,end="")
    print()
for i in range (1,n+1):
    for j in range(1,i):
        print(end=" ")
    for k in range(1,n+2-i):
        print(k,end="")
    for l in range(n-i,0,-1):
        print(l,end="")
    print()