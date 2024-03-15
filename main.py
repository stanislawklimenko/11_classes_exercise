# 1 Fill the missing pieces of the Calculator class
class Calculator:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def calculate_power(self):
        return self.var1 ** self.var2

    def calculate_sum(self, var3):
        return self.var1 + self.var2 + var3


calc = Calculator(2, 3)
assert calc.calculate_power() == 8
assert calc.calculate_sum(4) == 9


# 2 Finalize StringManipulator class
class StringManipulator:
    """This class reverse the place of the input string and make the title of the string"""

    category = "Manipulator"

    __doc__ = """Docstring of StringManipulator"""

    def __init__(self, original):
        self.string = original

    def reverse_words(self):
        words = self.string.split(' ')
        self.string = ' '.join(reversed(words))

    def make_title(self):
        self.string = self.string.title()
    # Create implementation for this

    def get_manipulated(self):
        return self.string

assert StringManipulator.__doc__ == "Docstring of StringManipulator"
assert StringManipulator.category == "Manipulator"

str_manip = StringManipulator("cOOL pyThON")

str_manip.reverse_words()
assert str_manip.get_manipulated() == "pyThON cOOL"

str_manip.make_title()
assert str_manip.get_manipulated() == "Python Cool"


# 3 Create Dog class
class Dog:
    # Your implementation here
    def __init__(self):
        self.energy = 10

    def get_energy(self):
        return self.energy

    def bark(self):
        self.energy -= 1

    def sleep(self):
        self.energy += 2


doge = Dog()
assert doge.get_energy() == 10

doge.bark()
doge.bark()
doge.bark()
assert doge.get_energy() == 7

doge.sleep()
assert doge.get_energy() == 9

another_doge = Dog()
assert another_doge.get_energy() == 10