products = []
counter = 1
command = ''
while command != "stop":
    name = input('name: ')
    price = input('price: ')
    amount = input('amount: ')
    units = input('units: ')
    products.append((counter, {"name": name, "price": price, "amount": amount, "units": units}))
    counter += 1
    command = input("Write 'stop' for stop inputting")
print(products)
result_dict = {}
for num, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_dict.get(key):
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)
for key, value in result_dict.items():
    result_dict[key] = list(set(value))
print(result_dict)
