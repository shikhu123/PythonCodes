name = 'Baby '
# reverse indexing
print(name[-2])
new_name = name[::3]
ne_name = name[1:]

print(new_name)
print(ne_name)
print(new_name + 'e')
print(name * 10)

print(name.upper())
print(name.lower())
print(name.split())

# string formatting

print('hello string {}'.format('insert'))

print('hello string {} {} '.format('insert', 'second'))
print('hello string {} {} {}'.format('insert', 'third', 'second'))

print('hello string {0} {2} {1}'.format('insert', 'third', 'second'))

print('hello string {i} {s} {t}'.format(i='insert', t='third', s='second'))
