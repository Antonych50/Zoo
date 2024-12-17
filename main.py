import abc

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
        return "Птица " + f"{self.name}, возраст {self.age}"

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
        return "Животное " + f"{self.name}, возраст {self.age}"


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
        return "Рептилия " + f"{self.name}, возраст {self.age}"

class Employes():

    def __init__(self, full_name, post):
        self.name = full_name
        self.post = post

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
    def add(self,worker):
        self.employes.append(worker)

    def __add__(self, animal):
        self.animals.append(animal)

    def remove(self,obj):
        if type(obj)
        try:
            self.employes.remove(worker)
        except ValueError:
            print("Такого работника зоопарка нет!")


    def remove(self, animal):
        try:
            self.animals.remove(animal)
        except ValueError:
            print("Такого животного в зоопарке нет!")

b = Bird("Grach", 1)
print(b.str_info())