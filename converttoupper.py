def firstupper(l):
    str=""
    if (ord(l[0]) >= 97 and ord(l[0]) <= 125):
        str+=chr(ord(l[0])-32)
    i=1
    while i<len(l):
        if((ord(l[i])>=97 and ord(l[i])<=125) or l[i]==" "):
            if(l[i]==" " and l[i+1]!=" "):
                str+=" "+chr(ord(l[i+1])-32)
                i+=2
            else:
                str+=l[i]
                i+=1
        else:
            str+=l[i]
            i+=1
    return str
line=input("Enter the string ")
print("The output is",firstupper(line))
