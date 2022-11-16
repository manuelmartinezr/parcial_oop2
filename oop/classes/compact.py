from .vehicle import Vehicle
class Compact(Vehicle):
    def __init__(self) -> None:
        self.size = 1
        self.parking_cost = 1