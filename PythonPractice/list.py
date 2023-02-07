from os import getcwd

my_list = ['list can contain different obejct/variable types', 1, 2, 3, 'four']
print(my_list)
my_list.append('five')  # will append variable at the end
print(my_list)
my_list.pop()  # will take out last element
print(my_list)

num_list = [0, 1, [1, 2]]
print(num_list[2][1])

# Sets
print(set('Mississippi'))
mylist = [1, 4, 5, 3, 2, 5, 4, 1]
print(set(mylist))
print(set('shikha'))
print(set([1, 1, 2, 3]))

getcwd()
