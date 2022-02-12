result = {}
with open('6.txt') as file:
    file_line = file.readlines()
    for line in file_line:
        data = line.split()
        # проверка всех возожных чисел
        hours = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'
                # запись числа
                for i in elem:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)



