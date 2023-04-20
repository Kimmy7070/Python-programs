import re
def incdate(cal):
    monthday={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    d,m,y=map(int,re.split("[.,/]",cal))
    s=cal[-5]
    if d == monthday[m] and m == 12:
        y+=1
        d=1
        m=1
    else:
        if d == monthday[m] and m != 2:
            d=1
            m+=1
        else:
            d+=1
    if m==2 and d == monthday[m]:
        if y%4==0 and y%100!=0:
            d+=1
        else:
            m+=1
            d=1
    date=str(d).zfill(2)+s+str(m).zfill(2)+s+str(y)
    return date
n=input("Enter the date to be incremented ")
print ("Next date is ",incdate(n))
