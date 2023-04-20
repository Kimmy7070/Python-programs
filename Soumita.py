n=int(input('enter the number'))
i=1
s=0
c=1
while c<=n:
	j=1
	f=1
	while j<=i:
		f=f*j
		j+=1
	if c%2!=0:
		s=s+f
	else:
		s=s-f
	i=i+2
	c=c+1
print(s)
