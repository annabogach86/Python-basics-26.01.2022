def int_funk(text):
    Text = text.capitalize()
    return Text

text = input('Введите текст: ')
text_list = text.split(' ')
for text in text_list:
    print(f'{int_funk(text)}', end=' ')
