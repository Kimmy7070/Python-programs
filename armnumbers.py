for i in range (100,1000):
    sum=0
    j=i
    while(j>0):
        sum+=(j%10)**3
        j//=10
    if(sum==i):
        print(i)
