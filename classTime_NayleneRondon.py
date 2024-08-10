#Naylene Rondon
#4/3/17
#Lab 8
class time():
    """Replicate Time"""
    def __init__(self):
        """Initizlize time."""
        self.hour = 0
        self.minute = 0
        self.period = ""

    def simpleTime(self):
        Time = (str(self.hour) + ":" + str(self.minute) + " " + self.period)
        return Time

    def statementTime(self):
        print("It is " + str(self.hour) + " hours and " + str(self.minute) + " minutes.")

    def simpleState(self):
        Time = self.simpleTime()

        print("The time is " + Time)
        



#Test statements

myTime = time()
myTime.hour = 11
myTime.minute = 38
myTime.period = "AM"
myTime.statementTime()
Time = myTime.simpleTime()

print("The time is " + Time)

myTime.simpleState()
