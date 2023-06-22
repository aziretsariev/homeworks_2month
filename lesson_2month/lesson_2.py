class Contacts:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

class Animal:
    def __init__(self, name, age, contacts):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age attribute '
                                 'it must be positive number')
        if isinstance(contacts, Contacts):
            self.__contacts = contacts
        else:
            raise ValueError('Wrong value for contacts attribute '
                                 'it must be of data type Contacts')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Wrong value for age attribute '
                             'it must be positive number')

    def info(self):
        return f'Name: {self.__name} Age: {self.__age}' \
               f' Birth year: {2023 - self.__age}\n' \
               f'ADDRESS: {self.__contacts.city}, {self.__contacts.street},' \
               f' {self.__contacts.number}'

    def speak(self):
        raise NotImplementedError('Method speak() must be implemented')

class Fish(Animal):
    def __init__(self, name, age, contacts):
        super(Fish, self).__init__(name, age, contacts)

    def speak(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, contacts):
        super(Cat, self).__init__(name, age, contacts)

    def speak(self):
        print('myauu')

class Dog(Animal):
    def __init__(self, name, age, commands, contacts):
        super(Dog, self).__init__(name, age, contacts)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super(Dog, self).info() + f'\nCommands: {self.commands}'

    def speak(self):
        print('gaav')

class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contacts):
        super(FightingDog, self).__init__(name, age, commands, contacts)
        self.__wins = wins

    @property
    def wins(self):
        return self.wins

    @wins.setter
    def wins(self, value):
        self.__wins = value
        
    def info(self):
        return super(FightingDog, self).info() + f'\nWins: {self.__wins}'


contact1 = Contacts('Bishkek', 'Toktogula', 147)

some_animal = Animal('Anim', 2, contact1)
some_animal.set_age(3)
print(some_animal.info())

dog = Dog('raks', 5, 'Sit', contact1)
dog.commands = 'Sit, Run'
print(dog.commands)

fightingdog = FightingDog('borzyi', 1, 'Fight', 8, contact1)

cat = Cat('Tom', 9, Contacts('Osh', 'lenina', 221))

fish = Fish('Dori', 2, contact1)


animals_list = [cat, dog, fish, fightingdog]
for animal in animals_list:
    animal.speak()
    print(animal.info())



