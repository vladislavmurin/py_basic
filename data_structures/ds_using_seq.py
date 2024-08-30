shoplist = ['5x40 oil', 'head gasket', 'spark plugs', 'oil filter']
name = 'to-do'

# indexing
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('\nCharacter 0 is', name[0])

# slicing on a list
print('\nItem 1 to 3 are', shoplist[1:3])
print('Item 2 to end are', shoplist[2:])
print('Item 1 to -1 are', shoplist[1:-1])
print('Item start to end are', shoplist[:])

# slicing on a string
print('\ncharacters 1 to 3 are', name[1:3])
print('characters 2 to end are', name[1:])
print('characters 1 to -1 are', name[1:-1])
print('characters start to end are', name[:])
