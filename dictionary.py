# dictionary eg
eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp) # print dict
print(eng2sp['two']) # print element of dict
print(len(eng2sp)) # print length of dict
print('one' in eng2sp) # determine an element in dict
vals = list(eng2sp.values())
print('uno' in vals)

#dictionary as set of counters
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

#looping and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])