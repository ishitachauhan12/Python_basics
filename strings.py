# string indexing
fruit = 'banana'
letter = fruit[1]
print(letter)

# string length
fruit = 'banana'
print(len(fruit))
length = len(fruit)
last = fruit[length-1]
print(last)

#traversing string
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

#string slices
s = 'Monty Python'
# indices are specified
print(s[0:5]) # 0 is includes and 5 is excluded

print(s[6:12]) # 6 is includes and 12 is excluded

# counting 'a'
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

print('a' in 'banana')

#string comparison
word = 'banana'
if word == 'banana':
    print('All right, bananas.')

word = 'pineapple'
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# string methods
stuff = 'hello world'
print(type(stuff))
print(dir(stuff))

word = 'banana'
new_word = word.upper()
print(new_word) 

word.find('na')
print(word.find('na', 3)) # index=3

line = '  Here we go  '
print(line.strip())

line = 'Have a nice day'
print(line.startswith('Have'))

# parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# format operator

camels = 42
print('%d' % camels)
print('I have spotted %d camels.' % camels)
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))