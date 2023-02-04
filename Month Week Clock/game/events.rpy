init python:
    class Calendar(object):
        def __init__(self, weekDays, Months, monthDays, Month, weekCounterDays, monthCounterDays, Hours, Hour):
            self.weekDays = weekDays
            self.Months = Months
            self.monthDays = monthDays
            self.Month = Month
            self.weekCounterDays = weekCounterDays
            self.monthCounterDays = monthCounterDays
            self.Hours = Hours
            self.Hour = Hour 

        @property 
        def Output(self):
            return self.weekDays[self.weekCounterDays] + " " + self.Months[self.Month] + " " + str(self.monthCounterDays+1) + " " + str(self.Hours).zfill(2)
            
        def AddTime(self, hours):
            self.Hours += hours
            if self.Hours > 23:
                self.Hours -= 24
                self.weekCounterDays += 1
                self.monthCounterDays +=1
            if self.weekCounterDays > 6:
                self.weekCounterDays = 0
            if self.monthCounterDays > self.monthDays[self.Month]:
                self.Month +=1
                self.monthCounterDays = 0
            if self.Month > 11:
                self.Month = 0
        
    class Event(object):
        def __init__(self, Hour, weekCounterDays, Month, Block, isActive):
            self.Hour = Hour
            self.weekCounterDays = weekCounterDays
            self.Month = Month
            self.Block = Block
            self.isActive = isActive
        def DateCheck(self, c):
            if self.weekCounterDays c.weekCounterDays and self.Hour == c.Hours and self.Month == c.Month:
                return True