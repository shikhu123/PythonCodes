# def solution(X, Y, A):
#     N = len(A)
#     r = -1
#     nX = 0
#     nY = 0
#     for i in range(N):
#         if A[i] == X:
#             nX += 1
#         elif A[i] == Y:
#             nY += 1
#         if nX == nY:
#             r = i
#         else:
#             return r
#
#
# print(solution(6,13,[13,13,1,6]))


class Dog:  # creating a class

    def __init__(self, breed):  # __init__ is the mthod for  instance of the class
        # attributes
        # we take in the arguments
        # assign it using self.attribute_name
        self.breed = breed  # breed is the parameter of argument and self.breed is attribute


my_dog = Dog(breed='Lam')


# print(my_dog.breed)


class Human:  # creating a class

    # class object attributes
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, gender, name, spots):  # __init__ is the mthod for  instance of the class
        # attributes
        # we take in the arguments
        # assign it using self.attribute_name
        # argument/parameter is string so it can be boolean , int , character
        self.mygender = gender  # breed is the parameter of argument and self.breed is attribute
        self.myname = name
        self.myspots = spots

    # operations/action  --> Methods
    def bark(self, number):
        print('woof! My name is {} and my number is {}'.format(self.myname, number))


my_human = Human(gender='F', name='shikha', spots=True)


# print(my_human.mygender)
# print(my_human.myname)
# print(my_human.myspots)
# print(my_human.species)
#
# my_human.bark(2)


class Circle:
    # class object attribute
    pi = 3.14

    # instance of a class circle
    def __init__(self, radius=1):
        self.radius = radius
        # for using attribute it's not necessary that parameter is in the function we can create new one like this
        # if its a class object attribute like pi we can call them by two ways Clas_name. attribute and self.attribute
        self.area = radius * radius * Circle.pi

    # method for the class circle
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()
# print(my_circle.pi)
# print(my_circle.radius)
print(my_circle.get_circumference())
