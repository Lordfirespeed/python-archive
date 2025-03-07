import datetime

sdate = datetime.date(2001, 1, 1)
edate = datetime.date(2099, 12, 31)

delta = edate - sdate

every = []
distinct = {}
for i in range(delta.days + 1):
    day = sdate + datetime.timedelta(days=i)
    string = str(day.day) + str(day.month) + str(int(str(day.year)[-2:]))
    every.append(string)
    if string in distinct.keys():
        distinct[string] += 1
    else:
        distinct[string] = 1

ans = ([v for v in distinct.values() if v > 1])
print(len(ans), sum(ans))
