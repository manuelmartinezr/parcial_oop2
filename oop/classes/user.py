from .vehicle import Vehicle
from .parking_lot import Parking_Lot

class User:
    def __init__(self, vehicle: Vehicle, lot: Parking_Lot) -> None:
        self.vehicle = vehicle
        self.lot = lot

    def register() -> None:
        pass