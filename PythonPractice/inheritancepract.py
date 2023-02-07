class Animal:  # base class

    def __init__(self):
        print('Animal Created')

    def eat(self):
        print('I am eating')

    def who_am_i(self):
        print('I am an animal')


class Dog(Animal):  # Derived class (Inherit animal class)

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print('I am huskie')


# I can inherit all the methods of Animal class in Dog class
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()




