# str object
name = 'somename'

if name.startswith('some'):
    print('Yes, string starts with "some"')

if 'a' in name:
    print('Yes, "a" contains in name')

if name.find('ome') != -1:
    print('Yes, name contains "ome"\n')

delimiter = '_*_'
mylist = ['5x40 Oil', 'Head Gasket', 'Oil Filter', 'Spark Plugs']
print(delimiter.join(mylist))
