line=input("Enter the numbers ")
a=line.split()
max=int(a[0])
min=int(a[0])
for i in a:
    if max<int(i):
        max=int(i)
    if min>int(i):
        min=int(i)
print("The difference is ",max-min)
