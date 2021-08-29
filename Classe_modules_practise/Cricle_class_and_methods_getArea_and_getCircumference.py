#  Create a Cricle class and intialize it with radius.
#  Make two methods getArea and getCircumference inside this class.

import math
class circle:
    def __init__(self, radius):
        print('this is tadius', radius)
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return 2 * math.pi * self.radius

area_of_circle = circle(3)

print(area_of_circle.getArea())
print(area_of_circle.getCircumference())