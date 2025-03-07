import datetime
from calendar import isleap
from scipy.constants import golden as phi
from math import e


def gettime(timestr):
    day = int(timestr[0])
    month = int(timestr[1])
    year = int(timestr[2:6])
    second = int(timestr[6:8])
    minute = int(timestr[8])
    hour = int(timestr[9])
    return datetime.datetime(year, month, day, hour, minute, second)


def getstr(num):
    return str(num).replace(".", "")[:10]


def elapsed(start, end):
    timepassed = end - start
    yearspassed = range(start.year, end.year + 1)
    for year in yearspassed:
        timepassed -= datetime.timedelta(1) if isleap(year) else datetime.timedelta(0)
    if isleap(start.year) and start.month > 2:
        timepassed += datetime.timedelta(1)
    if isleap(end.year) and end.month <= 2:
        timepassed += datetime.timedelta(1)

    return timepassed


phistring = getstr(phi)
estring = getstr(e)

phitime, etime = gettime(phistring), gettime(estring)

difference = elapsed(phitime, etime)

print("Seconds passed:", answer := int(difference.total_seconds()))
final = int((answer * 0.04) + 1689093)
print("Final Answer:", final)
