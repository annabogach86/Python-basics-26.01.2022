nums = {
        'One': "Один",
        'Two': "Два",
        'Tree': "Три",
        'Four': "Четыре"
}
with open('4.txt') as file, open('new_4.txt', 'w') as new_4:
    text_lines = file.readlines()
    for line in text_lines:
        data = line.split()
        rus_num = nums.get(data[0])
        new_4.write(f'{line.replace(data[0], rus_num)}')
