a={1:"A",2:"B",3:"C"}
print(a.get(1,4))
print(len(a))


b={"abc":4,"def":5,"ghi":7}
b.update({"xyz":4})
print(b)

dict={1,"A",2,"B"}
del dict
print(dict)
print(type(dict))

d = {"first":1, "second":2, "third": 3}
print(d.items())
print(list(d.keys()))

# s = dict([('first',1),('second',2),('third',3)])
# print(s) error
my_dict = {'apple': 3, 'banana': 6, 'cherry': 2}
sorted_keys = sorted(my_dict)
print(sorted_keys)

my_dict = {'a': 1, 'b': 2, 'c': 3}
result = my_dict.update({'d': 4})
print(result)