def my_func(arg_1, arg_2, arg_3):
    sum = (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)
    return sum

arg_1 = float(input('Введите первое число:'))
arg_2 = float(input('Введите второе число:'))
arg_3 = float(input('Введите третье число:'))
summa = f'Сумма двух наибольших чисел равна: {my_func(arg_1, arg_2, arg_3):.2f}'
print(summa)
