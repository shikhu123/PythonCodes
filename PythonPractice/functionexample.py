from random import shuffle


def even_num(num):
    return num % 2 == 0


def even_um(num, b):
    if num % b == 0:
        print(True)
        return True


def evn_l():
    c = int(input('first number'))
    d = int(input('Second number'))
    h = []
    for n in range(c, d):
        if n % 2 == 0:
            h.append(n)
        else:
            pass

    return h


# print(evn_l())


def even_list():
    a = [1, 2, 3, 4, 5, 1, 2, 4, 6, 8]
    for x in a:
        if x % 2 == 0:
            print(x)
        else:
            pass

    return False


def even_lst():
    a = [1, 2, 3, 4, 5, 4, 2, 6, 8]
    c = []
    for x in a:
        if x % 2 == 0:
            if x not in c:
                c.append(x)
        else:
            pass

    return c


# print(even_lst())


# print(even_num(37))

# different functions


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Select a number 0, 1 or 2")

    return int(guess)


def check_list(mylist, guess):
    if mylist[guess] == 'O':
        print('correct')

    else:
        print('incorrect')
        print(mylist)


mylist = ['', 'O', '']

mixed_list = shuffle_list(mylist)

guess = player_guess()

print(check_list(mixed_list, guess))
