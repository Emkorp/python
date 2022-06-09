
name = input('Enter name of product: ')
price = input('Enter price of product: ')
amount = input('Enter amount of product: ')
elements = input('Enter amount of product: ')
my_dict =  {'название': name, 'цена': price, 'количество': amount, 'ед.': elements}
for key, value in my_dict.items():
    print(f"{key} - {value}")
name2 = input('Enter name of product: ')
price2 = input('Enter price of product: ')
amount2 = input('Enter amount of product: ')
elements2 = input('Enter amount of product: ')
my_dict2 =  {'название': name2, 'цена': price2, 'количество': amount2, 'ед.': elements2}
for key, value in my_dict2.items():
    print(f"{key} - {value}")
