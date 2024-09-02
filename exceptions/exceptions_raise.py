class ShortInputException(Exception):
    '''a user-defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Entr smth: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('how dare u use EOF on me')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print("No exceptions raised.")
