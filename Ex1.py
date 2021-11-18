import json
import csv
import sys
import math
from Elevators import Elevators

if __name__ == "__main__":
    file = open(str(sys.argv[1]), )
    callsfile = open(str(sys.argv[2]), )
    op_f = open(str(sys.argv[3]), 'w', newline='')
    calls_str = list(csv.reader(callsfile, delimiter=','))
    output = csv.writer(op_f)
    building_str = json.load(file)
    elevators = Elevators(building_str)
    call_temp_list = []
    while calls_str:
        for current_elevator in elevators.elevatorsArray:
            elevator_speed = int(current_elevator['_speed'])
            if elevator_speed == 0:
                elevator_speed = elevator_speed + 1
            calls_division = int(len(calls_str) / (math.ceil(current_elevator['_speed'])))
            index = 0

            while len(calls_str) > 0 and (int(calls_str[0][2]) < current_elevator['_minFloor'] or int(calls_str[0][3]) >
                                          current_elevator['_maxFloor'] or int(calls_str[0][3]) < current_elevator[
                                              '_minFloor'] or
                                          int(calls_str[0][2]) > current_elevator['_maxFloor']):
                calls_str.pop(0)
            while index < elevator_speed and index*calls_division < len(calls_str):
                output.writerow([calls_str[index * calls_division][0], calls_str[index * calls_division][1],
                                 calls_str[index * calls_division][2], calls_str[index * calls_division][3],
                                 calls_str[index * calls_division][4], current_elevator['_id']])
                index = index + 1
            index = elevator_speed - 1
            while index >= 0 and index*calls_division < len(calls_str):
                calls_str.pop(index * calls_division)
                index = index - 1
