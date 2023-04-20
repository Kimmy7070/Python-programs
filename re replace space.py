import re
n=input("Enter the string")
p=" "
r=re.sub("\s+",p,n)
print(r)
