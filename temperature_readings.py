temps = [[(0.0) for hour in range(24)] for day in range(31)]
sum = 0.0

for day in temps:
    sum += day[12]
avg = sum / 31

print("Average temp at noon:", avg)



temps = [[0.0 for hour in range(24)] for day in range(31)]

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("Highest temp that month:", highest)

temps = [[0.0 for hour in range(24)] for day in range(31)]

hot_days = 0

for day in temps:
    if temp >= 20:
       hot_days += 1

print("The number of hot days that month:", hot_days)