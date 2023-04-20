f=open("abc.txt","r")
n=input("Enter the string you want to find :")
s=f.readlines()
for line in s:
    st=line.split()
    if n in st:
        print (line)
f.close()
