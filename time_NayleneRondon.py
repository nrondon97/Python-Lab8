#Naylene Rondon
#4/3/17
#Lab 8
class time():
    """Replicate Time"""
    def __init__(self, hour, minute, period):
        """Initizlize time."""
        self.hour = hour
        self.minute = minute
        self.period = period

    def simpleTime(self):
        Time = (str(self.hour) + ":" + str(self.minute) + " " + self.period)
        return Time

    def statementTime(self):
        print("It is " + str(self.hour) + " hours and " + str(self.minute) + " minutes.")

    def simpleState(self):
        Time = self.simpleTime()

        print("The time is " + Time)
        



#Test statements

myTime = time(11, 20, "AM")
myTime.statementTime()
Time = myTime.simpleTime()

print("The time is " + Time)

myTime.simpleState()
