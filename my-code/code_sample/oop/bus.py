from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_speed=100):
        super().__init__(starting_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(120)
bus1.add_warning('I am going to fast!!')
bus1.add_group(['Mark', 'Stacey'])
print(bus1)
bus1.drive()
print(bus1.get_warnings())
print(bus1.top_speed)
