#tuples eg
t = 'a', 'b', 'c', 'd', 'e'
#or
r = ('a', 'b', 'c', 'd', 'e')
print(t,r)
t1 = ('a',)
print(type(t1))
t = tuple('lupins')
print(t)
print(t[1:3])
t = ('A',) + t[1:]
print(t)

#comparing tuples
print((0, 1, 2) < (0, 3, 4))

# sorting text according to length:
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

#tuple assignment
m = [ 'have', 'fun' ]
x, y = m
print(x)
print(y)
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

# Dictionaries and tuples
d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
print(t)
t.sort()
print(t)

#list comprehension
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = []
for x in list_of_ints_in_strings:
    list_of_ints.append(int(x))

print(sum(list_of_ints))
