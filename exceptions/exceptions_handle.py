try:
    text = input('Ent smth: ')
except EOFError:
    print('how dare u put EOF on me?!')
except KeyboardInterrupt:
    print('u canceled it, congrats')
else:
    print('u entered {}'.format(text))
