rating_list = [7, 7, 6, 5, 5, 3, 2, 2, 2, 1]
rating = int(input('Введите новый элемент рейтинга: '))
flag = False
for index, element in enumerate(rating_list):
    if rating > element:
        rating_list.insert(index, rating)
        flag = True
        break
if not flag:
    rating_list.append(rating)
print(rating_list)
