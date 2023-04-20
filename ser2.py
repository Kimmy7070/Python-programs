n=int(input("Enter the limit"))
x=int(input("Enter the number"))
j=1
sum=0
for i in range (1,n+1):
    k=j
    f=1
    while k>0:
        f*=k
        k-=1
    if(i%2==0):
        sum-=((x**i)/f)
    else:
        sum+=((x**i)/f)
    j+=2
print(sum)
