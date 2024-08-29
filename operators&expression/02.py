age = 20
name = 'Bebeha'
hight = 900
width = 450

print('with width of {0} and hight of {1} \n{2} was literally a bookshelf'.format(width, hight, name))
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('8===========3') #ha, benis
print(name + ' is ' + str(age) + ' years old')

#OTHERWAY MUCH SHORTER(?)
print(f'{name} was {age} y/o and looked like a boockshelf \nbecause of hight and width = {hight} * {width}')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end=' ')
print('b', end=' ')
print('c', end=' \\prost\\')