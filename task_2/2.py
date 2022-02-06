def user_data(name, surname, year_birth, city, email, tel):
    return (f'name - {name}; surname - {surname}; year_birth - {year_birth}; city - {city}; email - {email}; tel - {tel}')

name = input('Name: ')
surname = input('Surname: ')
year_birth = int(input('Year of birth:'))
city = input('City: ')
email = input('E-mail: ')
tel = int(input('Telephone: '))
print(user_data(name, surname, year_birth, city, email, tel))
