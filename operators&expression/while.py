number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congrats!')
        running = False
    elif guess < number:
        print('biggah')
    else:
        print('smollah')
else:
    print('loop is over')

print('d o n e')
