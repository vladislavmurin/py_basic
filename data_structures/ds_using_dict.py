# ab = address book
ab = {
    'Ken': 'ken@miles.com',
    'Ben': 'ben@benny.com',
    'Noone': 'noone@none.com',
    'Spaaaaam': 'Spam@everytime.com',
}

print("Ken's email is: ", ab['Ken'])

# deleting
del ab['Spaaaaam']

print("\nThere're {} contacts in the AB\n".format(len(ab)))

for name, address in ab.items():
    print('Contacts {} at {}'.format(name, address))

# adding
ab['Dom'] = 'dom@tunna.com'

if 'Dom' in ab:
    print("\nDom's email is: ", ab['Dom'])
