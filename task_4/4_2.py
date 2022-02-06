def my_func(x, y):
    total = 1
    for i in range(abs(y)):
        total = total * x
    return (1 / total)

x = float(input('Введите положительное число:'))
y = int(input('Введите отрицательное число:'))
exp = f'Возведение числа x в степень y: {my_func(x, y):.5f}'
print(exp)
