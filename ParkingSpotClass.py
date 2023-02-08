# Senior Design
# Parking Spot Class

class ParkingSpot:
#coordinates [0] & [1] = Top left
#coordinates [2] & [3] = Top right
#coordinates [4] & [5] = Bottom right
#coordinates [6] & [7] = Bottom right
    def __init__(self, isOpen =  False, coordinates = (0,0,0,0,0,0,0,0)) :
        self.isOpen = isOpen
        self.coordinates = coordinates

