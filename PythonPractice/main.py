def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print('dumb test')

print((2 * 45) + 10)

print(len("hello"))

print('Hello World'[8])

print('tinker'[1:4])

print(
    ['Monty Python' if n % 6 == 0 else 'Python'
    if n % 3 == 0 else 'Monty'
    if n % 2 == 0 else n
    for n in range(1, 10)])
