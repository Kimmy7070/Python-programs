l = input ("Enter the String ")
n={}
for i in l:
    n[i]=n.get(i,0)+1
print (n)