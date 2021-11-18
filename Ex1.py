import csv
from src.elevatorAlgo import ElevatorAlgo
import sys

# take args
buildingFile = sys.argv[1]
callsFile = sys.argv[2]
outputFile = sys.argv[3]

# init algo
elevatorAlgo = ElevatorAlgo(buildingFile, callsFile, outputFile)

# copying calls csv file to an object
file = open(callsFile)
callsList = {}
i = 0
try:
    data = csv.reader(file)
    for row in data:
        callsList[i] = row
        i += 1
finally:
    file.close()

# allocating each call its best elevator
j = 0
for j in range(0, i):
    row = callsList.get(j)
    time = row[1]
    src = row[2]
    dest = row[3]
    allocatedElevator = elevatorAlgo.allocate(
        src, dest, time)
    # row[4] we can ignore
    row[5] = allocatedElevator

# copying proccessed calls object back to csv file
file = open(outputFile, "w", newline='')
j = 0
try:
    writer = csv.writer(file)
    for j in range(0, i):
        row = callsList.get(j)
        writer.writerow(row)
finally:
    file.close()