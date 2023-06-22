'''1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
2. Добавить сеттеры и геттеры к существующим атрибутам.
3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические
вычисления с атрибутами объекта cpu и memory.
4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
5. Добавить сеттеры и геттеры к существующему атрибуту.
6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number,
в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например:
если при вызове метода передать число 1 и номер телефона, распечатывается текст
“Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал
симуляцию проложения маршрута до локации.
9. В каждом классе переопределить магический метод str которые бы возвращали полную информацию об объекте.
10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было
сравнивать между собой объекты, по атрибуту memory.
11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
12. Распечатать информацию о созданных объектах
13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call,
а также магические методы)'''


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f"Cpu: {self.cpu}, memory: {self.memory}"

    def make_computations(self):
        a = self.cpu + self.memory
        b = self.cpu - self.cpu
        c = self.cpu * self.memory
        d = self.cpu // self.memory
        return f"cpu {self.cpu} + memory {self.memory} = {a}\n" \
               f"cpu {self.cpu} - memory {self.memory} = {b}\n" \
               f"cpu {self.cpu} * memory {self.memory} = {c}\n" \
               f"cpu {self.cpu} // memory {self.memory} = {d}\n"

    def __gt__(self, other):
        return self.cpu > self.other

    def __ge__(self, other):
        return self.cpu >= self.other

    def __eq__(self, other):
        return self.cpu == self.other


class Phone:
    def __init__(self, sim_card_list: list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def __str__(self):
        return f"sim card list: {self.sim_card_list}"

    def call(self, sim_card_number, call_to_number):
        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number
        return f"идёт звонок на номер: {self.sim_card_number} с сим-карты: {self.sim_card_list[self.call_to_number]}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        self.location = location
        return f"проложен маршрут до: {self.location}"

    def __str__(self):
        return f'cpu: {self.cpu} memory: {self.memory} sim card list: {self.sim_card_list}'


asus = Computer(23, 32)
iphone = Phone(['Beeline', 'O!'])
print(iphone.call('0987654', 0))
samsung = SmartPhone(600, 32, ["Beeline", "o!", "MegaCom"])
huawei = SmartPhone(650, 16, ["Beeline", "o!", "MegaCom"])
print(samsung.use_gps("Цум"))
print(asus.make_computations())
print(asus)
print(iphone)
print(samsung)
print(huawei)

