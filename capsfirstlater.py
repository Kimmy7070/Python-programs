def upr(ch):
    if ch >= 'a' and ch <= 'z':
        ch=chr(ord(ch)-32)
    return ch
n=input("Enter the sentence ")
s=upr(n[0])
for i in range (1,len(n)):
    if n[i-1]==' ' and n[i]!=' ':
        s+=upr(n[i])
    else:
        s+=n[i]
print(s)