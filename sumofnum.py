def sumofnum(n):
    if(n>0):
        return n%10 + sumofnum(n//10)
    else:
        return 0
n=int(input("Enter the number "))
print("The sum of number is ",sumofnum(n))
