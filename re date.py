import re
s="today is 51-06-2021 and tomorrow is 22/06/2021 023/4/2000"
'''p="\d{2}[-/.]\d{2}[-/.]\d{4}"'''
p="[0-3][0-9][-/.][0-1][0-9][-/.]\d{4}"
r=re.findall(p,s)
print (r)
