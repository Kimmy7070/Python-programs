def f():
    yield 5
    yield 6
    yield 7
x=f()
print(next(x))
print(next(x))
print(next(x))
'''
for i in f():
    print(i)
'''
