# For and if else Loop
from random import randint
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 8, 3, 4, 2, 1, 4]
newlist = []

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(num)

for num in mylist:
    if num not in newlist:
        newlist.append(num)
        print(num)

# different method
newlist1 = set(mylist)
print(newlist1)

# tuple example
newlist2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in newlist2:
    print(b)

# dictionary example
newlist3 = {'k1': 1, 'k2': 2, 'k3': 4}
for item in newlist3:
    print(item)

for item in newlist3.items():
    print(item)

for key, values in newlist3.items():
    print(key, values)

for key, values in newlist3.items():
    print(values)

for values in newlist3.values():
    print(values)

# While Loop
n = [1, 2, 3, 4]
for i in n:
    pass
print("testing pass statement")

m = 'gundeep'
for l in m:
    if l == 'n':
        continue
    print(l)

a = 0
while a < 5:
    if a == 4:
        break
    print(a)
    a += 1

# operators

# range

x = 0
for x in list(range(3, 10)):
    print(x)

print(list(range(2, 10, 2)))

index_count = 0
for letter in 'abcdesfghj':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

# enumerate

for letter in enumerate('abcdefgh'):
    print(letter)

for index, letter in enumerate('abcdefgh'):
    print(index)
    print(letter)
    print('\n')

# ZIP

mlist = [1, 2, 3, 5, 6]
nlist = ['a', 'c', 'd', 'r', 'f']
for item in zip(mlist, nlist):
    print(item)

# in
g = 'a' in 'word'
print(g)

# Max
print(max(mlist))

# min
print(min(mlist))

# random
# shuffle
shuffle(mlist)
print(mlist)

# randint
k = randint(0, 100)
print(k)

# input

s = int(input('what is your fav num'))
print(s)

# List Comprehensions

# here we can do appending without using append method

w = 'dhikssh'
comp = [letter for letter in w]
print(comp)

com = [x for x in 'word']
print(com)

q = [x for x in range(0, 10)]
print(q)

# sqaure of every number
e = [x**2 for x in range(0, 10)]
print(e)

# even numbers
r = [x for x in range(0, 10) if x % 2 == 0]
print(r)

# odd num
t = [x for x in range(0, 10) if x % 2 != 0 ]
print(t)