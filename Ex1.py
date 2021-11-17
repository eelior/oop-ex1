import json
import csv
import sys

from Elevators import Elevators


def allocate(call, elevators_obj):
    callDst = int(call[3])
    callSrc = int(call[2])
    best_proximity = 99999
    chosenElevator = 0
    if elevators.num_of_elevators == 1:
        return elevators_obj.elevatorsArray[0]['_id']

    for i in elevators_obj.elevatorsArray:
        curr_proximity = abs(callSrc - i['_currFloor'])

        if best_proximity >= curr_proximity:
            best_proximity = curr_proximity
            chosenElevator = i['_id']
            # print("best proximity is" + curr_proximity+"and elev id is "+i['_id'])

    i['_currFloor'] = callDst
    return chosenElevator


if __name__ == "__main__":

    file = open(str(sys.argv[1]), )
    callsfile = open(str(sys.argv[2]), )
    op_f = open(str(sys.argv[3]), 'w', newline='')
    calls_str = csv.reader(callsfile, delimiter=',')
    output = csv.writer(op_f)
    building_str = json.load(file)

    elevators = Elevators(building_str)
    # elevators.print()
    # j = 0;
    for i in calls_str:
        output.writerow([i[0], i[1], i[2], i[3], i[4], allocate(i, elevators)])

    # for i in building_str['_elevators']:
    #     print(i['_id'])
