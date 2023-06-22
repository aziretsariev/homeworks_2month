'''ДЗ*:
1. Создать класс Person с атрибутами fullname, age, is_married
2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем,
где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
6. Добавить в класс Teacher атрибут уровня класса salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле:
к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика,
эти ученики добавляются в список и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с
его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.'''

class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"{self.fullname} \n{self.age}\n{self.is_married}")

    def __str__(self):
        return f"Name:{self.fullname}\n" \
               f"Age:{self.age}\n" \
               f"Marriage:{self.is_married}\n"

person2 = Person("Tasia", 22, True)
print(person2.introduce_myself())


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks


    def avarege(self):
        print(sum(self.marks) // len(self.marks))


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 10000

    def new_salary(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary
        else:
            print('Стаж меньше 3 лет')

k = Teacher("aigerim", "yes", True, 10)
print(f"{k.fullname},{k.salary},{k.age},{k.is_married}")
print(k.new_salary())


def create_students():
    student1 = Student("Dan", 13, False, marks={
        "история": 2,
        "алгебра": 5,
        "физра": 3,
        "физика": 4,
        "химия": 5
    })
    student2 = Student("Ben", 15, False, marks={
        "история": 4,
        "алгебра": 5,
        "физра": 4,
        "физика": 4,
        "химия": 5
    })
    student3 = Student("Alex", 25, True, marks={
        "история": 5,
        "алгебра": 3,
        "физра": 5,
        "физика": 4,
        "химия": 5
    })

    result = [student1, student2, student3]
    return result


student = create_students()
for i in student:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name:{i.fullname}\n"
          f"Age:{i.age}\n"
          f"Marriage:{i.is_married}\n"
          f"Average:{sum(list) / len(list)}\n")