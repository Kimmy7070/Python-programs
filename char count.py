import string
def count (line):
    c=0
    v=0
    w=0
    p=0
    d=0
    for i in range (len(line)):
        if line[i] in "aeiou" or line[1] in "AEIOU":
            v+=1
        elif line[i] in string.punctuation:
            p+=1
        elif line[i] in string.whitespace:
            w+=1
        elif line[i] in string.digits:
            d+=1
        else:
            c+=1
    return v,c,p,w,d
l=input("Enter the line ")
v,c,p,w,d=count(l)
print("The vowels =",v,"The consonanats =",c,"The puncutations =",p,"The whitespace =",w) 
