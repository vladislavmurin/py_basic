class Robot:
    """Represents a robot, with a name"""

    # class variable counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data..."""
        self.name = name
        print("(Initializing {})".format(self.name))

        Robot.population += 1

    def relocate(self):
        """I've been relocated."""
        print('{} is being relocated.'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one here and was successfully relocated.'.format(self.name))
        else:
            print('There are still {:d} robots working here.'.format(
                Robot.population))

    def say_hi(self):
        """Greetings by the robot.

        Yap, we can do that."""
        print('Greeting, work is calling me {}'.format(self.name))

    @classmethod
    def how_many(cls):
        """Prints population"""
        print('We have {:d} robots'.format(cls.population))


droid1 = Robot("mk1")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("mk2")
droid2.say_hi()
Robot.how_many()

print('\nRobots are ready.\n')

print("Robots have been finished. Let's transfer them.")
droid1.relocate()
droid2.relocate()

Robot.how_many()
