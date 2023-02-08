import time


# t = time()

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour *= 60
mins += hour
mins *= 60
sec = mins

secString = ""



mins += dura
result = hour, ":", mins
stringResult = ""

# def endTime(sec):
    
#     return stringResult




# def stringTimeInSecs(sec):
#     return secString


