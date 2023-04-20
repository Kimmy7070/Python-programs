line=input("Enter the numbers")
a=line.split()
p=[]
n=[]
for i in a:
    if int(i)>=0:
        p.append(int(i))
    else:
        n.append(int(i))
print("Positive list")
for i in p:
    print(i,end=" ")
print()
print("Negative list")
for i in n:
    print(i,end=" ")
