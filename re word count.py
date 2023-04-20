import re
n=input("Enter the string ")
p="\w+"
r=re.findall(p,n)
print(r)
