class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Oi, my name is', self.name)

p = Person('Ben')
p.say_hi()
