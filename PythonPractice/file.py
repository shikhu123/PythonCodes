x = open('myfile.txt', 'w')
x.write('This is my second file')
x.close()

with open('test.txt', mode='w') as f:
    print(f.write('hi'))


