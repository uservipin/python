class laptop:

    def __init__(self, company, processor, ram):
        parameter = 'test this parameter'
        self.company = company
        self.processor = processor
        self.ram = ram
        self.on = False

    print('print laptop class')

    def modelNo(self):
        self.on = True
        print('laptop is ON')

    def Off(self):
        self.on = False

    def features(self, company, processor, ram):
        print(self.Company, self.processor, self.ram)


class Ac:
    def __init__(self, brand, capacity):
        print("It's too hot , lets turn on the Ac")
        self.Brand = brand
        self.Capacity = capacity
        self.status = "off"

    def on(self):
        if self.status == "off":
            self.status = "on"
            print("Ac is on")
        else:
            print("Ac is already on!")

    def Off(self):
        if self.status == "on":
            self.status = "off"
            print('Ac has been turned off')
        else:
            print('Ac is already off')

    def setmode(self, mode='Auto'):
        if self.status == "on":
            if mode == "Auto":
                self.temp = 25
                print('Auto mode activated and temp is', self.temp)
            elif mode == "Cool":
                self.temp = 18
                print("Cool mode activated and temp is", self.temp)
            elif mode == 'Hot':
                self.temp = 28
                print('Hot mode activated and temp is', self.temp)

    def increase_temp(self):
        self.temp += 1
        print('Temp is', self.temp)

    def decrease_temp(self):
        self.temp -= 1
        print('Temp is', self.temp)

ac1=Ac('Voltas',2.5)
ac1.on()

ac1.setmode('Hot')
