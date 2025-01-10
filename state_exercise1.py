from abc import ABC,abstractmethod


class Elevator():
    def __init__(self,floor, capacity):
        self.floor = floor
        self.capacity = capacity
        self.flow = [floor.current_floor]




class Move():
    def __init__(self, elevator):
        self.elevator = elevator
        self.floor = elevator.flow[-1]

    def movement(self, destination):
        self.destination = destination
        if destination in self.elevator.floor.allowed_floors:
            self.direction = "+" if self.floor < self.destination else "-"
            print(f"elevator is moving to {self.destination}")
            self.elevator.floor.current_floor = self.destination
        else:
            print("error!!")



class Floor():
    def __init__(self, initail_floor):
        self.current_floor = initail_floor


    allowed_floors = ["g",1,2,3,4,5,6,7,8]

floor = Floor(initail_floor=4)
print(floor.current_floor)
elv = Elevator(floor, capacity=6)
mv1 = Move(elv)
mv1.movement(6)


