# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x.startswith('s'):
        print(x)

e = [x for x in st.split() if x.startswith('s')]
print(e)

# Use range() to print all the even numbers from 0 to 10.

# method 1
print([x for x in range(0, 10) if x % 2 == 0])

# method 2
print([x for x in range(0, 11, 2)])

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print([i for i in range(1, 50) if i % 3 == 0])

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x) % 2 == 0:
        print(x+'||'+'even')

d = [x for x in st.split() if len(x) % 2 == 0]
print(d)

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1, 100):
    if x % 5 == 0 and x % 3 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
y = [x[0] for x in st.split()]
print(y)
