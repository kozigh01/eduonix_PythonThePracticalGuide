simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)
del simple_list[1]
print(simple_list)


d = {'name': 'Max', 'age': 33}
print(d.items())
for k, v in d.items():
    print(k, v)
del d['age']
print(d)


t = (1, 2, 30)
print(t.index(30))
# del t[2]  # throws error - tuples are immutable


s = {'Max', 'Anna', 'Max'}
s.add('Bob')
print(s)
s.discard('Anna')
print(s)


l = [1, 2, 3, 4, -5]
l_valid = all([n > 0 for n in l])
print(l_valid)
l_valid = any([n < 0 for n in l])
print(l_valid)