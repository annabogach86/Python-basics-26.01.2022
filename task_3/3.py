with open('3.txt') as file:
    text_lines = file.readlines()
    dictionary = {}
    sum_salary = 0
    for line in text_lines:
        dict_info = line.split()
        dictionary.update({dict_info[0]: float(dict_info[1])})
        sum_salary += float(dict_info[1])
average_salary = sum_salary / len(dictionary)
print(f'Average = {average_salary:.2f}')
for k, v in dictionary.items():
    if v < 20000:
        print(f'{k}: {v}')
