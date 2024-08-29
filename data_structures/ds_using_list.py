shoplist = ['muffler', 'head gasket', '550 fuel injectors', 'fuel pump']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, ';', end=' ')

print('\nI also have to buy an air filter')
shoplist.append('air filter')

print('I will sort my shopping list')
shoplist.sort()
print('Sorted shopping list looks like:')

print('The first item to buy is', shoplist[3])
olditem = shoplist[3]
del shoplist[3]
print('I bought the', olditem)
print('My shopping list now is:', shoplist)