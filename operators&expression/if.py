number = 23
guess = int(input('Enter an integer : '))

if  guess == number:
    print('Congrats!')
    print('But there is no prize, go to another castle')
elif guess < number:
    print('wrong, number must be biggah')
else:
    print('naaah mate, try little bit smollah')
print('Aye, we"r done here')