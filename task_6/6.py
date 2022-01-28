a, b = int(input('Введите км: ')), int(input('Введите км: '))
counter = 1
print(f'{counter}' + '-й день:', f'{a:.2f}')
while a < b:
    a = (a * 0.1) + a
    counter += 1
    print(f'{counter}' + '-й день:', f'{a:.2f}')
print('На', f'{counter}' + '-й день спортсмен достиг результата, не менее', f'{a:.0f}', 'км')
