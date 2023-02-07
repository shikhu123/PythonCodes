import random

def gensquares(n):
    for x in range(n):
        yield x**2


# for x in gensquares(10):
#     print(x)


def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
     print(num)


s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


my_list = [1,2,3,4,5]
def gencomp():
    for index, item in enumerate(my_list):
        if item > 3:
         yield item

for item in gencomp():
    print(item)



