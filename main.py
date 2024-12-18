import abc
import os
import re
from os.path import split


class Animal(abc.ABC):

    @abc.abstractmethod
    def make_sound(self):
        raise NotImplementedError

    @abc.abstractmethod
    def eat(self):
        raise NotImplementedError

    @abc.abstractmethod
    def str_info(self):
        raise NotImplementedError

class Bird(Animal):
    movement = "flying"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Bird sings: 'Chick-chirick'")

    def eat(self):
        return "Seeds"

    def str_info(self):
        return f"{self.name}, {self.age}"

class Mammal(Animal):
    movement = "walking"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Animal say: 'B-r-r'")

    def eat(self):
        return "Compound feed"

    def str_info(self):
        return f"{self.name}, {self.age}"


class Reptile(Animal):
    movement = "crawling"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Reptile say: 'Sh-sh-sh'")

    def eat(self):
        return "Midge"

    def str_info(self):
        return f"{self.name}, {self.age}"

class Employes():

    def __init__(self, full_name, post):
        self.name = full_name
        self.post = post

    def str_repr(self):
        return f"{self.name}, {self.post}"

class ZooKeeper(Employes):
    def __init__(self, full_name, post="zookeeper"):
        super().__init__(full_name, post)

    def feed_animal(self):
        print("Кормит животных")

class Veterinarian(Employes):
    def __init__(self, full_name, post="veterinarian"):
        super().__init__(full_name, post)

    def feed_animal(self):
        print("Лечит животных")

class Zoo():
    employes = []  # список сотрудников
    animals =[] # список животных
    def __init__(self):
        pass
    @staticmethod
    def add_worker(full_name, post="zookeeper"):
        Zoo.employes.append(f"{full_name}, {post}")

    @staticmethod
    def add_animal(name, age):
        Zoo.animals.append(f"{name}, {age}")

    @staticmethod
    def remove(text):
        s = split(text)
        pattern = r'[0-9]+/b'
        if re.match(pattern,s[1]):#Найдено число во второй части текста, т.е. текст описывает животное
            try:
                Zoo.animals.remove(text)
            except ValueError:
                print("Такого животного в зоопарке нет!")
        else:
            try:
                Zoo.employes.remove(text)
            except ValueError:
                print("Такого работника зоопарка нет!")

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)

with open(current_directory+"/Employes.txt", 'r', encoding='utf-8') as f:
        Zoo.employes = f.readlines()
        for i in range(len(Zoo.employes)):
            Zoo.employes[i] = Zoo.employes[i].strip()

print(f"{Zoo.employes}")

with open(current_directory + "/Animals.txt", 'r', encoding='utf-8') as f:
    Zoo.animals = f.readlines()
    for i in range(len(Zoo.animals)):
        Zoo.animals[i] = Zoo.animals[i].strip()
print(f"{Zoo.animals}")
Zoo.add_worker("Кузмичев Кузьма Кузьмич")
print(f"{Zoo.employes}")
b = Bird("Grach", 1)
s = split(b.str_info())
Zoo.add_animal(s[0], s[1])
print(f"{Zoo.animals}")
Zoo.remove("Алексеев Алексей Алексеевич, veterinarian")
print(f"{Zoo.employes}")
Zoo.remove("Поросёнок, 0.5")
print(f"{Zoo.animals}")
#Сохраняем возможные изменения в списках сотрудников и животных
with open(current_directory+"/Employes.txt", 'w', encoding='utf-8') as f:
    f.writelines(Zoo.employes)

with open(current_directory + "/Animals.txt", 'w', encoding='utf-8') as f:
    f.writelines(Zoo.animals)

