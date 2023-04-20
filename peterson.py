n=int(input("Enter a number"))
j=n
sum=0
while(j>0):
    r=j%10
    f=1
    while(r>0):
        f*=r
        r-=1
    sum+=f
    j//=10
if(sum==n):
    print("Peterson number")
else:
    print("Not Peterson number")
