def lin_search():
    line=input("Enter the numbers ")
    a=line.split()
    x=input("Enter the number needed for search")
    for i in a:
        if x == i:
            print(x," is found in position ",a.index(i)+1)
def bin_search():
    line=input("Enter the numbers in sorted manner ")
    a=line.split()
    x=int(input("Enter the number needed for search"))
    l=len(a)-1
    f=0
    while f<=l:
        mid=(f+l)//2
        if int(a[mid])== x:
            print(x," is found in position ",a.index(str(x))+1)
            break
        elif x > int(a[mid]):
            f=mid+1
        else:
            l=mid-1
def bub_sort():
    line=input("Enter the numbers")
    a=line.split()
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if int(a[j])>int(a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print("The sorted list ")
    for i in a:
        print(i,end=" ")
def sel_sort():
    line=input("Enter the numbers")
    a=line.split()
    for i in range(len(a)):
        min = a[i]
        pos = i
        for j in range(i+1,len(a)):
            if int(min) > int(a[j]):
                min=a[j]
                pos = j
        if i != pos:
            a[i],a[pos]=a[pos],a[i]
    print("The sorted list ")
    for i in a:
        print(i,end=" ")
def ins_sort():
    line=input("Enter the numbers")
    a=line.split()
    for i in range(len(a)):
        n=a[i]
        j=i-1
        while j>=0 and n<=a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=n
    print("Sorted list")
    for i in a:
        print(i,end=" ")
def merge():
    line1=input("Enter list 1")
    a=line1.split()
    line2=input("Enter list 2")
    b=line2.split()
    for i in b:
        a.append(i)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if int(a[i])>int(a[j]):
                 t=a[j]
                 a[j]=a[i]
                 a[i]=t
    print("The merged list ")
    for i in a:
        print(i,end=" ")
print("Enter the number of the function you want")
print("1. Linear search \n2. Binary search/n3. Bubble Sort\n4. Selection Sort\n5. Insertion Sort\n6. Merge two sorted list")
n=int(input())
if n==1:
    lin_search()
elif n==2:
    bin_search()
elif n==3:
    bub_sort()
elif n==4:
    sel_sort()
elif n==5:
    ins_sort()
elif n==6:
    merge()
else:
    print("Error")
