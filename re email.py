import re
n=input("Enter the email string ")
p="[\w.]+@[\w.]+[.][com|in]+"
r=re.findall(p,n)
print(r)
