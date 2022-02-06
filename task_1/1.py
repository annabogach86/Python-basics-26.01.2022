def division_func(num_1, num_2):
    if num_2 == 0:
        return 'На ноль делить нельзя!'
    else:
        div = num_1 / num_2
    return div

num_1 = float(input('Введите первое число:'))
num_2 = float(input('Введите второе число:'))
division = f'{division_func(num_1, num_2):.2f}'
print(division)
