import re
l=input("Enter the string")
while l != ' ':
    s=l[0]
    count = 0
    print(s,end='-')
    for i in range (1,len(l)):
        if s==l[i]:
            count += 1
            l=l[:i]+l[i+1:]
    print (count)
