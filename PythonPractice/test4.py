class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


# EXAMPLE OUTPUT
coor1 = (3, 2)
coor2 = (8, 10)

li = Line(coor1, coor2)
print(li.distance())
print(li.slope())


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * pow(self.radius, 2) * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * (self.radius + self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


acct1 = Account('Jose', 100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(500)
acct1.withdraw(75)

