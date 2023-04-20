n = int(input("Enter the limit"))
i = 0
for j in range(1, n+1):
    if j % 2 == 0:
        i = i*10+2
    else:
        i = i*10+1
    print(i,end=" ")