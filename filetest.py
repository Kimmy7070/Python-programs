f=open("abc.txt","r")
n=input("Enter the string you want to find :")
s=f.readlines()
line=0
while line < len(s):
    st=s[line].split()
    if n in st:
        print (s[line],end="")
    line+=1
f.close()
