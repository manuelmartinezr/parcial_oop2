from .vehicle import Vehicle
class Van(Vehicle):
    def __init__(self) -> None:
        self.size = 3
        self.parking_cost = 3