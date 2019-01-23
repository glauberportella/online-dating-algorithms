from time import (localtime, mktime, strftime, strptime)


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


def strTimeProp(start, end, format, prop):
    stime = mktime(strptime(start, format))
    etime = mktime(strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return strftime(format, localtime(ptime))
