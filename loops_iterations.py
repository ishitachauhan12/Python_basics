# updating variables
x = 10
print(x)
x = x + 1
print(x)

# while statment
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# #infinite loop with break
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# # Finishing iterations with continue
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# for loop
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

for friend in friends:
    print('Happy New Year:', friend)

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

# get largest and smallest in the loop

#get max
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

#get min
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)