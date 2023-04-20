f=open("abc.txt","r")
st=f.read().split()
n={}
for i in st:
    n[i]=n.get(i,0)+1
print(n)
f.close()
