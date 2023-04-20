n=input("Enter a name ")
abr = n[0]
for i in range (1,len(n)):
    if n[i]==' ' and n[i+1]!=' ':
        abr+="."+n[i+1]
        j=i+1
abr+=n[j+1:]
print("Name ",abr)