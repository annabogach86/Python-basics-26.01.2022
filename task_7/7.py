def my_factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        yield total
n = int(input('Введите числло: '))
for index, number in enumerate(my_factorial(n)):
    print(f'{index + 1}: {number}')

