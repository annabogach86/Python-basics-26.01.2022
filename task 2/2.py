my_list = input('Введите список: ')
my_list_split = my_list.split()    # делеим список на пробелы
my_list_len = len(my_list_split)    # рассчитываем кол-во символов в списке
total = 0
if my_list_len > 1:
    while total < (my_list_len - 1):
        my_list_split[total], my_list_split[total + 1] = my_list_split[total + 1], my_list_split[total]
        total += 2
print(my_list_split)
