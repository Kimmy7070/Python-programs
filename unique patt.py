n=int(input("Enter the limit"))
l=["X"]
for i in range(1,n+1):
    for j in l:
        print(j,end="")
    print()
    if (l[0]=="X" or l[0]=="O"):
        l.insert(0," ")
    elif (l[0]==" " and l[1]=="X"):
        l.insert(0,"O")
    else:
        l.insert(0,"X")
    
