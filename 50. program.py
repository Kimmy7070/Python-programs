def ptl (a,n):
    while n>0:
        print(a,end="")
        return ptl(a,n-1)
    return ""
print("What do you wanna print")
print("a) a line with 50 dots(.)")
print("b) a line with 50 @")
print("c) a line with 80 dots(.)")
print("d) a line with 70 #")
o=input()
if o=="a":
    print(ptl(".",50))
elif o=="b":
    print(ptl("@",50))
elif o=="c":
    print(ptl(".",80))
elif o=="d":
    print("#",70)
else:
    print(ptl(".",50))