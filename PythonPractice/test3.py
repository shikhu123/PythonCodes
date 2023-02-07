from itertools import count


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
    elif a % 2 != 0 and b % 2 != 0 and a > b:
        return a


# print(lesser_of_two_evens(2, 4))


# print(lesser_of_two_evens(5, 4))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    m = []
    for a in text.split():
        m.append(a)
    print(m)
    if m[0][0] == m[1][0]:
        return True
    else:
        return False


# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False

def makes_twenty(n, e):
    if n + e == 20 or n == 20 or e == 20:
        return True
    else:
        return False


# print(makes_twenty(20, 10))
# print(makes_twenty(12, 8))
# print(makes_twenty(2, 3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    a = ''
    for index, letter in enumerate(name):
        if index == 0:
            a += letter.upper()
        elif index == 3:
            a += letter.upper()
        else:
            a += letter.lower()

    return a


# print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    a = text.split()
    return ' '.join(a[::-1])


# print(master_yoda('I am home'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n, ):
    if n in range(90, 110) or n in range(100, 110) or n in range(190, 210):
        return True
    else:
        return False


# print(almost_there(150))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    h = []
    for num in h:
        pass


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    a = ""
    for index, letter in enumerate(text):
        a += letter * 3

    return a


print(paper_doll('hello'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


def blackjack(a, b, c):
    s = a + b + c
    if s <= 21:
        return s
    elif s > 21 and a == 11 or b == 11 or c == 11:
        f = s - 10
        return f
    elif s > 21:
        return 'BUST'
    else:
        pass


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting
# with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(arr):
    for arr in range(6, 9):
        pass


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(nums):


def count_primes(num):
    if num > 1:
        for n in range(2, num):
            if n % n == 0:
                pass
            else:
                print(n)

    return count(n)


print(count_primes(100))
