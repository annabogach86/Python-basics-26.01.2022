with open('2.txt') as file:
    text_line = file.readlines()
    str_counter = 0
    for num, line in enumerate(text_line):
        str_counter += 1
        words_counter = len(line.split())
        print(f'#{num + 1} - {words_counter} words')
    print(f'{str_counter} strings')
