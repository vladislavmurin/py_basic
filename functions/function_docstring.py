def print_max(x, y):
    """Prints the maximum of two numbers.

    Two values must be integers"""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is biggah')
    else:
        print(y, 'is biggah')


print_max(5, 6)
print(print_max.__doc__)
