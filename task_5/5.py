def my_funk(stroka, Enter):
    stroka_list = stroka.split()
    summa_str = 0
    for i in stroka_list:
        if i == Enter:
            break
        summa_str += int(i)
    return summa_str


stop = '$'
summa = 0
finish = False
while not finish:
    stroka = input('Введите строку чисел через пробел: ')
    summa += my_funk(stroka, stop)
    finish = stop in stroka
    print(f'Сумма чисел равна: {summa}')

