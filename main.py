import add_time

print("Enter time in the format:\nTime 1 -> (hh:mm AM/PM)\nTime 2 -> (hh:mm)\n")
time_1 = input("Enter Time 1: ")
time_2 = input("Enter Time 2: ")
day = input("Enter Day | Press(Enter) to skip |: ")

if day == '':
    day = None

myresult = add_time.add_time(time_1, time_2, day)

print(myresult)