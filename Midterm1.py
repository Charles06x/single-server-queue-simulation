import numpy as np
from delayTimeFunction import delayTime
from statistics import *

jobs = np.loadtxt("data.txt", delimiter='    ')
arrives = jobs[:,0]
services = jobs[:,1]

d = delayTime(arrives, services)
averageInterarrival, arrivalRate = averageInterarrival(arrives)
averageService, serviceRate = averageService(services)
averageDelay = averageDelay(d)
averageWait = averageWait(d, services)
jobsInServiceNode = little_jobsInServiceNode(d, services)
jobsInQueue = little_jobsInQueue(d)
jobsInService = little_jobsInService(services)
print("##########################################")
print("##########################################")
print("############ Statistics ##################")
print("##########################################")
print("##########################################")

print("\nAverage interarrival time: {} | Arrival rate: {}".format(averageInterarrival, arrivalRate))
print("\nAverage service time: {} | Service rate: {}".format(averageService, serviceRate))
print("\nAverage delay: ", averageDelay)
print("\nAverage wait: ", averageWait)

print("Time used in service node: ", jobsInServiceNode)
print("Time used in queue: ", jobsInQueue)
print("Time used in service: ", jobsInService)
