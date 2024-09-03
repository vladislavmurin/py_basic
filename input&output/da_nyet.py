ENUM_DA = 'da'
ENUM_NET = 'net'

a = input('Print svoyu huynyu: ').lower()

if a == ENUM_NET:
    print('pidora otvet')
elif a == ENUM_DA:
    print('pizda')
else:
    print(f"tut tolko 2 variata '{ENUM_DA}' ili '{ENUM_NET}', poetomy idinahuy")
