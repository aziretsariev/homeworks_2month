from random import randint as generate_number, choice
import calculator as calc
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 5))
print(calc.addition(2, 9))

my_friend = Person('Jim', 33)
print(my_friend)

cprint("Hello, World", "green", "on_red")
print(emoji.emojize("Python is fun :red_heart:"))

print(config('DATABASE_URL'))
num = config('COMMENTED', default=5, cast=int)
print(num * 2)