l=input ("Enter the String ")
n={}
words=l.split()
for i in words:
    n[i]=n.get(i,0)+1 
print(n)
