import re
n=input("enter a string ")
p=re.findall('www[.]{1}\w+[.]{1}com|org|in',n)
print(p)
