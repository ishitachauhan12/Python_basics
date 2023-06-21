# list eg
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
new = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(cheeses, numbers, empty, new)

# lists is mutable
numbers = [17, 123]
numbers[1] = 5
print(numbers)

#traversing in list
for cheese in cheeses:
    print(cheese)

#list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print([0] * 4)
print([1, 2, 3] * 3)

#list slice
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#list method
t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)

t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

#lists and functions
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#getting an average
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Lists and strings
s = 'spam'
t = list(s)
print(t) 
s = 'pining for the fjords'
t = s.split()
print(t)
#You can call split with an optional argument called a delimiter that 
#specifies which characters to use as word boundaries. The following 
#example uses a hyphen as a delimiter:

s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))

# parsing lines
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

# objects and values
a = 'banana'
b = 'banana'
print(a is b)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

#Aliasing
a = [1, 2, 3]
b = a
print(b is a)

#list arguments
def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)