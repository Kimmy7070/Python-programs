n=int(input("Enter the limit "))
sum=0
j=1
for i in range (1,n+1):
      fact=1
      for k in range (1,j+1):
          fact*=k
      sum+=fact
      j+=2
print("Sum",sum)