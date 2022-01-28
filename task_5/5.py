proceeds = int(input('Введите значение выручки фирмы: '))
cost = int(input('Введите значение издержек фирмы: '))
if proceeds > cost:
    print('Фирма работает с прибылью!')
    print('Рентабельность фирмы равна: ', ((proceeds - cost) / proceeds) * 100, '%')
    worker = int(input('Введите численность сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника равна: ', (proceeds - cost) // worker)
else:
    print('Фирма работает в убыток!')
    