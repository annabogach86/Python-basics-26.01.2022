def user_data(name, surname, year_birth, city, email, tel):
    user_data_dict = {'name': a, 'surname': b, 'year_birth': c, 'city': d, 'email': e, 'tel': f}
    return user_data_dict
a = input('Name: ')
b = input('Surname: ')
c = input('Year of birth: ')
d = input('City: ')
e = input('E-mail: ')
f = input('Telephone: ')
result = user_data(name=a, surname=b, year_birth=c, city=d, email=e, tel=f)
print(result)
