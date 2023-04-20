n = int(input("Enter a number"))
sum=0
k=1
for i in range (1,n+1):
    f=1
    j=k
    while j>0:
        f*=j
        j-=1
    if(i%2==0):
        sum-=f
    else:
        sum+=f
    k+=2
print(sum)
