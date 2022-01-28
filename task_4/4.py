n = int(input('Введите число: '))
total = 0
max_digit = 0
while n > 0:
    last_digit = n % 10
    total = last_digit
    if total > max_digit:
        max_digit = total
    n //= 10
print('Самая большая цифра в числе:', max_digit)
