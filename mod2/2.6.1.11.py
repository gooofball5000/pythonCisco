# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))


hour = 12
mins = 17
dura = 59

mins += dura
result = hour, ":", mins

def endTime(time):
    return result


print(hour, ":")
print(endTime)
