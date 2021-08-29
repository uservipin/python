# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them.
# E.g.- # (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
        def __init__(self,hours,minutes):
            self.hours= hours
            self.minutes= minutes
            self.total_minute =0
            self.minutes_and_hour=0
            # print(self.hours)
            # print(self.minutes)

        def addTime(time_1,time_2):
            #print('Both times are: ',time_1,time_2)
            # print('Minutes are :',time_1.minutes)
            # print('Minutes_if hours are :', time_1.hours*60)
            # print('Minutes are :', time_2.minutes)
            # print('Minutes_if hours are :', time_2.hours * 60)

            total_minute = time_1.minutes +time_1.hours*60 +time_2.minutes+time_2.hours * 60
            #print('total Minutes are : ',total_minutes)
            minutes_and_hour = [total_minute//60,total_minute%60]
            # return minutes_and_hour[0], minutes_and_hour[1]

        def total_minutes(self):
            return self.total_minute

        def minutes_and_hours(self):
            return self.minutes_and_hour

t1 = Time(3,40)
t2 = Time(4,50)
t3 =Time.addTime(t1,t2)




