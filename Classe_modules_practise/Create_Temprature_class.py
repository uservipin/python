#  Create a Temprature class. Make two methods :
#  1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#  2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temprature:

    # def __init__(self,temp):
    #     print('Temperature is ',temp)
    #     self.temp = temp
    #

    def celsius(self,celsius):
        celsius= (celsius-32)*5/9
        return celsius
    def Fahrenheit(self,fahrenheit):
        fahrenheit= (fahrenheit)*9/5+32
        return fahrenheit

temp =Temprature()

print(temp.celsius(23))
print(temp.Fahrenheit(-5))