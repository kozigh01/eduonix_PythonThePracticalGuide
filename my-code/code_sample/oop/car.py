from vehicle import Vehicle

class Car1:
    top_speed = 100

    def drive(self):
        print('I am driving, but not faster than {}'.format(self.top_speed))


my_car = Car1()
my_car.drive()

other_car = Car1()
other_car.drive()

other_car.top_speed = 150
my_car.drive()
other_car.drive()

Car1.top_speed = 200

my_car.drive()
other_car.drive()

print("-" * 30)


class Car2(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)

    # def __repr__(self):
    #     print('Printing <Car>.....')
    #     return f'<Car> Top Speed: {self.top_speed:^20}, Warnings: {self.__warnings}'

    # def add_warning(self, warning_text):
    #     if len(warning_text) > 0:
    #         self.__warnings.append(warning_text)

    # def get_warnings(self):
    #     return self.__warnings
    
    # def drive(self):
    #     print('I am driving, but not faster than {}'.format(self.top_speed))

    def brag(self):
        print('My car rocks!')


my_car = Car2()
# my_car.__warnings.append('New warnning')  # don't use the private property
my_car.add_warning('Another warning')
my_car.drive()
print(my_car)
print(my_car.__dict__)

other_car = Car2()
other_car.drive()

other_car.top_speed = 150
my_car.drive()
other_car.drive()

Car2.top_speed = 200
other_car.brag()

my_car.drive()
other_car.drive()
print(Car2.top_speed)
print(my_car.get_warnings())
print(other_car.get_warnings())
