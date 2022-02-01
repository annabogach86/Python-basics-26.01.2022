month = int(input('Введите номер месяца: '))
win, spr, sam, aut = 'winter', 'spring', 'summer', 'autumn'
season_list = [win, win, spr, spr, spr, sam, sam, sam, aut, aut, aut, win]
print(season_list[month - 1])
