n=input("Enter a string ")
c=1
for i in range (len(n)):
    if n[i]==' ' and n[i+1]!=' ':
        c+=1
print("Number of word ",c)