import abc
class Parking_Lot():
    def __init__(self) -> None:
        pass

class Vehicle(abc):
    size: int
    parking_cost: int

class Compact(Vehicle):
    def __init__(self) -> None:
        super().__init__()

class SUV(Vehicle):
    def __init__(self) -> None:
        super().__init__()

class Van(Vehicle):
    def __init__(self) -> None:
        super().__init__()

class User():
    pass