import math
import random

# build-in functions
print(max('Hello world'))
print(min('Hello world'))
print(len('Hello world'))

# Type conversion
print(type(int(3.99999)))

print(type(float(32)))
print(type(float('3.14159')))

print(type(str(32)))
print(type(str(3.14159)))

# Math functions
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians)) 

# random
for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10)) #low and high

t = [1, 2, 3]
print(random.choice(t)) #choose from t

# adding new functions
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

print_lyrics()   

# parameter and argument
def print_twice(bruce): #bruse is the parameter to which 'Spam' is assigned
    print(bruce)
    print(bruce) 

print_twice('Spam') #'Spam' is an argument