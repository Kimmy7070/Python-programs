line=input("Enter string ")
rev=""
for i in line:
    rev=i+rev
if rev==line:
    print("Pallindrome")
else:
    print("Not Pallindrome")
