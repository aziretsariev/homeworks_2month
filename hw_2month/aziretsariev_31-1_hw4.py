import  random
from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    HEAL = 1
    BOOST = 2
    CRITICAL_DAMAGE = 3
    BLOCK_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super(Boss, self).__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super(Hero, self).__init__(name, health, damage)
        if isinstance(ability, SuperAbility):
            self.__ability = ability
        else:
            raise ValueError('Wrong value')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def use_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def use_super_power(self, boss, heroes):
        coeff = random.randint(2, 6)
        boss.health -= self.damage * coeff
        print(f'Warrior hits criticaly: {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost_points):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost_points = boost_points

    def use_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                boss.health -= self.__boost_points


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def use_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def use_super_power(self, boss, heroes):
        self.__blocked_damage = 25
        if boss.damage == 50:
            boss.health -= self.__blocked_damage

        if boss.damage == 50:
            self.health += 25


round_number = 0


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.use_super_power(boss, heroes)
    show_stats(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_stats(boss, heroes):
    print(f'ROUND {round_number} ---------------')
    print(boss)
    for hero in heroes:
        print(hero)


def start_game():
    boss = Boss('Rashan', 1000, 50)
    warrior = Warrior('Hercules', 280, 10)
    magic = Magic('Rubik', 290, 15, 20)
    doc = Medic('Aibolit', 250, 5, 15)
    berserk = Berserk('Pudge', 220, 10)
    assistant = Medic('Hous', 300, 10, 5)
    heroes_list = [warrior, magic, doc, berserk, assistant]

    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()