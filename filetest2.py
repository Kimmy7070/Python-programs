f=open("abc.txt","rb")
l1=f.read()
print(l1)
f.seek(0,0)
l2=f.readline()
print(l2)
n=f.tell()
print(n)
f.seek(10,1)
l2=f.readlines()
print(l2)
f.seek(-10,2)
print(f.read())
f.close()
