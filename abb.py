n=input("Enter the name ")
a=n.split()
abb = ""
l=len(a)
for i in range (l-1):
    abb += a[i][0] + ". "
abb += a[l-1]
print("Name ",abb)
