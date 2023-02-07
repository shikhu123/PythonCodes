class Dog:  # creating a class

    def __init__(self, name):  # __init__ is the mthod for  instance of the class
        # attributes
        # we take in the arguments
        # assign it using self.attribute_name
        self.name = name  # breed is the parameter of argument and self.breed is attribute

    def speak(self):
        return self.name + ' says woof!'


class Cat:  # creating a class
    def __init__(self, name):  # __init__ is the method for  instance of the class
        # attributes
        # we take in the arguments
        # assign it using self.attribute_name
        self.name = name  # name is the parameter of argument and self.name is attribute

    def speak(self):
        return self.name + ' says meow!'


niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

# first example of polymorphism

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())


# another example of polymorphism

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)

pet_speak(felix)

case number: Hrc10846845

