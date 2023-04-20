f=open("abc.txt","r")
n=int(input("Enter number of lines "))
for i in range (n):
    s=f.readline()
    print(s)
f.close()
