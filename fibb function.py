def fibb(a,b,n):
    c=a+b
    if(n>=1):
        print(a,end=" ")
        fibb(b,c,n-1)
    else:
        return(0)
n=int(input("Enter the limit "))
fibb(0,1,n)