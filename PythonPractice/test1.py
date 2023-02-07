from math import sqrt

# Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
print(10**2/5*1+90.25-10)



# What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5))

# What is the value of the expression 4 * 6 + 5
print(4 * 6 + 5)

# What is the value of the expression 4 + 6 * 5
print(4 + 6 * 5)

# What is the type of the result of the expression 3 + 1.5 + 4?
# float
print(3 + 1.5 + 4)

# What would you use to find a number’s square root, as well as its square?
print(sqrt(3))
print(3 ** 2)

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1])

# Reverse the string 'hello' using slicing:
s = 'shikhahello'
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
s = 'hello'
# Method 1:
print(s[4])
# Method 2:
print(s[-1])

# LIST
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
print(list3)
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
print(set(list4))


# Dictionaries
d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# TUPLE
newlist = (1, 2, 3, 4, 5, 6)
print(newlist)

# SET
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))
