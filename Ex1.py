import json
import csv
import sys
import math
from Elevators import Elevators

if __name__ == "__main__":
    # reading the input files from the users
    file = open(str(sys.argv[1]), )
    callsfile = open(str(sys.argv[2]), )
    op_f = open(str(sys.argv[3]), 'w', newline='')
    building_str = json.load(file)

    # creating a list from the calls
    calls_str = list(csv.reader(callsfile, delimiter=','))

    # create an output file
    output = csv.writer(op_f)

    elevators = Elevators(building_str)

    # go through the calls
    while calls_str:

        # check which elevator fits best and allocate the call to it
        for current_elevator in elevators.elevatorsArray:

            # workload distribution between the elevators by it's speed
            elevator_speed = int(current_elevator['_speed'])
            if elevator_speed == 0:
                elevator_speed = elevator_speed + 1
            calls_division = int(
                len(calls_str) / (math.ceil(current_elevator['_speed'])))
            index = 0
            while index < elevator_speed and len(calls_str):
                output.writerow([calls_str[index*calls_division][0], calls_str[index*calls_division][1], calls_str[index*calls_division]
                                [2], calls_str[index*calls_division][3], calls_str[index*calls_division][4], current_elevator['_id']])
                index = index + 1
            index = elevator_speed - 1
            while index >= 0 and calls_str:
                calls_str.pop(index * calls_division)
                index = index - 1
