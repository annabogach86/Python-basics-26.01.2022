my_list = input('Введите строку: ')
words = my_list.split()
counter = 0
for word in words:
    counter += 1
    print(counter, f'- {word[:10]}')
