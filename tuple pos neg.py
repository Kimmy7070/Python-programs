l=input('Enter the element')
n=l.split()
int(n)
for i in n:
    if i >0:
        p.append(n[i])
    else:
        n.append(n[i])
p=tuple(p)
n=tuple(n)
print("Positive")
for i in p:
    print(i)
print("Negative")
for i in n:
    print(i)
