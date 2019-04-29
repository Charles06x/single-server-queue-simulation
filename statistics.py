from numpy import mean
#######Job-averaged statistics
def averageInterarrival(a):
    r = mean(a)
    aR = 1/r
    return r, aR

def averageService(s):
    s = mean(s)
    sR = 1/s
    return s, sR
def averageDelay(delay):
    d = mean(delay)
    return d

def averageWait(d, s):
    w = mean(d) + mean(s)
    return w

#######Time-averaged statistics

#Ew
def little_jobsInServiceNode(d, s):
    w = 0.0
    for i, j in zip(d, s):
        w+=(i+j)
    return w

#Ed
def little_jobsInQueue(d):
    sumD = 0.0
    for i in d:
        sumD+=i
    return sumD

#Es
def little_jobsInService(s):
    sumS = 0.0
    for i in s:
        sumS+=i
    return sumS
