import datetime
import re

date_list = ['2019-02-10', '2018-01-13', '2019-02-8',]

numPattern = re.compile("[0-9]+")


def getclosest(dates):
    global numPattern
    now = datetime.date.today()
    diffs = []

    for day in date_list:
        year, month, day = [int(i) for i in re.findall(numPattern, day)]
        currcheck = datetime.date(year, month, day)
        diffs.append(abs(now - currcheck))

    return dates[diffs.index(min(diffs))]
