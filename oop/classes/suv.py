from .vehicle import Vehicle
class SUV(Vehicle):
    def __init__(self) -> None:
        self.size = 2
        self.parking_cost = 2