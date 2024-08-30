print('Simple Assignment\n')
shoplist = ['5x40 oil', 'oil filter', 'air filter', 'spark plugs']

# adding "mylist" as another name for "shoplist"
mylist = shoplist

# I've purchased first item, so it can be removed
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# both lists w/o first item

print('\nCopy by making a full slice\n')
mylist = shoplist[:]
# removing first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# now this 2 lists are different
