import string
f=open("abc.txt","r")
st=f.read()
c=0
d=0
v=0
w=0
p=0
for i in range (len(st)):
    if st[i].isalpha():
        if st[i] in "aeiou":
            v+=1
        else:
            c+=1
    elif st[i].isdigit():
        d+=1
    elif st[i] in string.whitespace:
        w+=1
    elif st[i] in string.punctuation:
        p+=1
print("Number of digits:",d)
print("Number of consonants:",c)
print("Number of vowels:",v)
print("Number of white space:",w)
print("Number of punctuation:",p)
f.close()