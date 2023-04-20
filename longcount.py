l=input("Enter the sentence")
a=l.split()
max=0
for i in a:
    if len(i) > max :
        max= len (i)
print("The longesr word lenght is",max)