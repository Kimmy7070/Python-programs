import os
f=open("abc.txt","r")
s=f.read()
a=s.split()
b=" ".join(a)
f2=open("save.txt","w")
f2.write(b)
f.close()
f2.close()
os.remove("abc.txt")
os.rename("save.txt","abc.txt")