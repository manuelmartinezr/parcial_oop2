class Parking_Lot():
    def __init__(self, slots_compact: int, slots_suv: int, slots_van: int,
                time_open: list) -> None:
        self.slots_compact: int
        self.slots_suv: int
        self.slots_van: int
        self.time_open: list
        self.user_reservations = []

    @property
    def slots_compact(self):
        return self.slots_compact

    @property
    def slots_suv(self):
        return self.slots_suv
    
    @property
    def slots_van(self):
        return self.slots_van

    def refresh_list(self):
        pass