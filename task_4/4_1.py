def my_func(x, y):
    exp = x ** y
    return exp

x = float(input('Введите положительное число:'))
y = int(input('Введите отрицательное число:'))
exp = f'Возведение числа x в степень y: {my_func(x, y):.5f}'
print(exp)
