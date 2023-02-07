# exercise 1

def myfunc1():
    print('Hello World')


myfunc1()

# exercise 2

#name = 'Hello Name'


def myfunc2(name):
    print('my name is {}'.format(name))


#myfunc2(name)


# exercise 2


def name_k(name):
    print('hello {}'.format(name))


print(name_k('Shikha'))


# Exercise 3
#  If True, return 'Hello', and if False, return 'Goodbye'


def myfunc3(value):
    if value == True:
        return 'Hello'
    else:
        return 'Goodbye'


print(myfunc3(True))


# Exercise 4
# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.


def myfunc4(x, y, z):
    if z == True:
        return x
    else:
        return y


print(myfunc4('hello', 'outside', True))


# Exercise 5
# add two number


def myfunc5(a, b):
    return a + b


print(myfunc5(3, 5))


# Exercise 6
# even number


def myfunc6(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(myfunc6(40))


# Exercise 7
# Define a function called is_greater that takes in two arguments, and returns True
# if the first value is greater than the second, False if it is less than or equal to the second.

def myfunc7(d, e):
    if d > e:
        return True
    else:
        return False


print(myfunc7(4, 4))
