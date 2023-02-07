def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)



def gen_fibonacci(n):
    a =1
    b =1
    for i in range(n):
        yield a
        a,b = b, a+b

for h in gen_fibonacci(10):
    print(h)


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))