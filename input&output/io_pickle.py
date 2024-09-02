import pickle

shoplistfile = 'shoplist.data'
shoplist = ['oil 5x40', 'oil filter', 'air filter']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
f.close()
