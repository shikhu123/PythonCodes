# Problem 1 Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print("string can't be square root ")

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
#  in ()
#       1 for i in ['a','b','c']:
# ----> 2     print(i**2)
#
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# # Problem 2 Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
#
try:
    x = 5
    y = 0
    z = x / y
    print(z)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("All Done")


# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
#  in ()
#       2 y = 0
#       3
# ----> 4 z = x/y
#
# ZeroDivisionError: division by zero
# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
#
def ask():
    while True:
        try:
            num = int(input("Enter an int: "))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
    print("Square root", num ** 2)

#
#
ask()
# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is:  4
# Great Job!
