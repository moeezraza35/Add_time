class Time:
    def __init__(self, time):
        self.hour = ""
        self.mins = ""
        colon = False
        space = False
        h12 = ""
        for char in time:
            if char != ':' and char != ' ' and not colon and not space:
                self.hour += char
            elif char != ':' and char != ' ' and colon and not space:
                self.mins += char
            elif str(char).upper() == 'A' and str(char).upper() == 'P' and colon and space:
                h12 = char+'M'
            elif char == ' ':
                space = True
            else:
                colon = True
        self.hour = int(self.hour)
        self.mins = int(self.mins)

        if h12 == 'PM' and self.hour < 12:
            self.hour += 12

        while self.mins > 60:
            self.mins -= 60
            self.hour += 1
        

def findDay(day, num):
    days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    week_no = days.index(day)
    week_no += num

    while(week_no > 7):
        week_no -= 7

    return str(days[week_no]).capitalize()


def add_time(time_1, time_2, day):
    Time1 = Time(time_1)
    Time2 = Time(time_2)

    Total_hours= Time1.hour + Time2.hour
    Total_mins = Time1.mins + Time2.mins
    Total_days = 0

    Total_time = Time(str(Total_hours)+':'+str(Total_mins))

    while(Total_time.hour > 24):
        Total_time.hour -= 24
        Total_days += 1

    myResult = str(Total_hours)+':'+str(Total_mins)

    if day != None:
        Day = findDay(str(day).lower(), Total_days)
        myResult += f" ({Day})"
    if Total_days > 1:
        myResult += f"{str(Total_days)} days later"
    elif Total_days == 1:
        myResult += " next day"

    return myResult