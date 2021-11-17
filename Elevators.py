class Elevators:
    elevatorsArray = []
    num_of_elevators = 0
    def __init__(self,building_file):
        num_of_elevators = 0
        for i in building_file['_elevators']:
            i['_currFloor'] = i['_minFloor']
            i['_direction'] = "idle"
            self.elevatorsArray.append(i)
            num_of_elevators = num_of_elevators+1


    def print(self):
        for i in self.elevatorsArray:
            print(i)