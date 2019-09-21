import math
from ErrorChecking import ErrorChecking as EC

# Not my code


class Dest:  # returns the destination x,y coordinates given a current position, direction and distance
    def getDestination(self, currentPos, direction, distance):
        EC().check(direction, "int")  # checking if arguments are of correct type
        EC().check(distance, "int")
        EC().check(currentPos, "list")
        direction = float(direction)
        # Compute the change in position
        delta_y = distance * math.cos(math.radians(direction))
        delta_x = distance * math.sin(math.radians(direction))
        # Add that to the existing position
        new_x = currentPos[0] + delta_x
        new_y = currentPos[1] + delta_y
        return new_x, new_y
