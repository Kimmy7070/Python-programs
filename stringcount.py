line=input('Enter the string')
v=0
c=0
d=0
for i in line:
    if i in 'aeiou':
        v+=1
    elif i.isalpha() and i not in 'aeiou':
        c+=1
    elif i.isdigit():
        d+=1
print("Vowels:",v,"Consonants:",c,"Digit:",d)
