# def funct():
#     return 1
#
# # print(funct())
#
# def hello():
#     print("Hi jose")
#
# # hello()
#
# greet = hello
# # greet()
#
# # return function and return as a argument also
# def other(some_def_func):
#     print('other code runs here')
#     print(some_def_func())
#
# #other(hello)
#
#
# def new_decorator(original_func):
#     def wrap_func():
#         print("Some extra code, before the original code")
#         original_func()
#         print(" \t some extra code after the original function")
#
#     return wrap_func
#
# @new_decorator
# def func_needs_decorator():
#     print("I want to be decorated")
#
# # func_needs_decorator()
#
# decorated_func = new_decorator(func_needs_decorator())
# decorated_func()


def number(a):
 for i in a:
    if not i.isnumeric():
        print("Not a Number")
    else:
       print("Is a Number")

# for execute
number('10')
number('1ab')
