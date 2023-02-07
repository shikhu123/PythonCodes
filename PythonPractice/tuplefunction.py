def tpl():
    example = [('a', 10), ('b', 20), ('c', 30)]
    for d, e in example:
        print(d)
        print(e)
        print('\n')


print(tpl())

sample = [('a', 10), ('b', 20), ('c', 30)]


def unpcktl(sample):
    maxhour = 0
    employeename = ''
    for employee, hours in sample:
        if hours > maxhour:
            maxhour = hours
            employeename = employee

        else:
            pass

    return (employeename, maxhour)


print(unpcktl(sample))


