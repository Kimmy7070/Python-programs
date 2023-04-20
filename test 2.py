def f():
    i=1
    while i <101:
        yield i
        i+=1
for i in f():
    print (i)
