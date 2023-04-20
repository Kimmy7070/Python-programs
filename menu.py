while True:
    print("What do you want to do?")
    print("1.Centigrade to Fahrenheit")
    print("2.Fahrenheit to Centigrade")
    print("3.Centigrade to Reaumur")
    print("4.Reaumur to Centigrade")
    print("5.Reaumur to Fahrenheit")
    print("6.Fahrenheit to Reaumur")
    print("Enter respective values,use 0 to exit")
    c=int(input())
    if c==0:
        break
    n=int(input("Enter the value to be converted"))
    if c==1:
        r=n*9/5+32
    elif c==2:
        r=(n-32)*5/9
    elif c==3:
        r=n*4/5
    elif c==4:
        r=n*5/4
    elif c==5:
        r=n*9/4+32
    elif c==6:
        r=(n-32)/9*4
    print("The output value is ",r)