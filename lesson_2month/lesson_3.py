from enum import Enum

class Color(Enum):
    BLUE = '\33[34m'
    RED = '\33[31m'
    YELLOW = '\33[33m'


class MusicPlayable: # mixin

    @staticmethod
    def play_music(model, song):
        print(f'Now is playing {song} in {model}')

    @staticmethod
    def stop_music(model):
        print(f'Music stopped in {model}')


class SmartPhone(MusicPlayable):
    def __init__(self):
        pass


class Car(MusicPlayable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError('Wrong value')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year


    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return f'MODEL: {self.__model} YEAR: {self.__year}' \
               f' COLOR: {self.__color.value}{self.__color.name}' + '\33[0m'


    def __gt__(self, other):
        return nissan_car.__year > other.__year

    def __lt__(self, other):
        return nissan_car.__year < other.__year

    def __le__(self, other):
        return nissan_car.__year <= other.__year

    def __ge__(self, other):
        return nissan_car.__year >= other.__year

    def __eq__(self, other):
        return nissan_car.__year == other.__year

    def __ne__(self, other):
        return nissan_car.__year != other.__year


class FuelCar(Car):
    __total_fuel_amout = 1000

    @classmethod
    def get_total_fuel_amout(cls):
        return cls.__total_fuel_amout

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    def __init__(self, model, year, fuel_bank, color):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amout -= self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super(FuelCar, self).__str__() + f' FUEL_BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value


class ElectricCar(Car):
    def __init__(self, model, year, battery, color):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using battery')

    def __str__(self):
        return super(ElectricCar, self).__str__() + f' BATTERY {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, fuel_bank, battery, color):
        FuelCar.__init__(self, model, year, fuel_bank, color)
        ElectricCar.__init__(self, model, year, battery, color)


print(f'Before: {FuelCar.get_total_fuel_amout()}')

nissan_car = FuelCar('Nissan Skyline', 2009, 65, Color.RED)
print(nissan_car)

tesla_car = ElectricCar('Tesla Model S', 2022, 25000, Color.BLUE)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2000, 50, 10000, Color.YELLOW)
print(toyota_car)
toyota_car.drive()

print(f'Car Nissan is newer then Car Tesla {nissan_car > tesla_car}')
print(f'Car Nissan is newer then Car Tesla {nissan_car < tesla_car}')
print(f'Car Nissan is newer then Car Tesla {nissan_car != tesla_car}')

print(f'Before: {FuelCar.get_total_fuel_amout()} {FuelCar.get_fuel_type()}')
tesla_car.play_music(tesla_car.model, 'Song 1')
tesla_car.stop_music(tesla_car.model)

samsung = SmartPhone()
samsung.play_music('Samsung S23', 'Best Song')

if tesla_car.model == 'Tesla Model S':
    print('This car is cool')

if tesla_car.color == Color.BLUE:
    print('This car is beautiful')