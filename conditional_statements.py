################# conditional execution
x = 10
if x > 0 : # 'if' condition ended by a ':'
    print('x is positive')

################# alternative execution
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

################# chained conditionals
x = 10
y = 11

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

################# Nested conditionals
x = 14
y = 7
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

################# Catching exceptions using try and except

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

################# guardian pattern
x = 6
y = 2

print(x/y) 
#this code will break when y=0 as division by 0 is undefined

y=0
#use guard code
print(y>0 and x/y)

