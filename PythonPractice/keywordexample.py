# *args (argument - arbitary arguments(tuple))  and  **kwargs(keyword arguments - pass_dictonary)

# Exercise 1

# Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those
# arguments.


def myfunc1(*args):
    return sum(args)


print(myfunc1(2, 4, 5, 6))


# Exercise 2

# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only
# those arguments that are even.

def myfucn2(*args):
    return [i for i in args if i % 2 == 0]


print(myfucn2(1, 2, 4, 5, 6, 3, 7))


# Exercise 3
# Define a function called myfunc that takes in a string, and returns a matching string where every even
# letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters,
# and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or
# lowercase letter, so long as letters alternate throughout the string.

def funct3(name):
    a = ''
    for index, letter in enumerate(name):
        if index % 2 == 0:
            a += letter.upper()
        else:
            a += letter.lower()

    return a


print(funct3('shikha'))
