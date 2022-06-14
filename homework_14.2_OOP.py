

# Hometask_14_5
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит
# конструктор и методы: run, jump,
# birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный
# метод fly, Cat - meow, Dog - bark.


# class Dog:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def jump(self):
#         return f"Dog can jump"
#
#     def run(self):
#         return f"Dog can run"
#
#     def bark(self):
#         return f"Dog can bark"
#
#     def sleep(self):
#         return f"Dog can sleep"
#
#     def birthday(self):
#         return self.age + 1
#
# class Cat:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def jump(self):
#         return f"Cat can jump"
#
#     def run(self):
#         return f"Cat can run"
#
#     def meow(self):
#         return f"Cat can meow"
#
#     def sleep(self):
#         return f"Cat can sleep"
#
#     def birthday(self):
#         return self.age + 1
#
# class Parrot:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def jump(self):
#         return f"Parrot can jump"
#
#     def run(self):
#         return f"Parrot can run"
#
#     def fly(self):
#         return f"Parrot can fly"
#
#     def sleep(self):
#         return f"Parrot can sleep"
#
#     def birthday(self):
#         return self.age + 1
#
# if __name__ == '__main__':
    # Jack = Dog("Jack", 3, "Tom")
    # print(Jack.name, Jack.age, Jack.master)
    # print(Jack.run())
    # print(Jack.jump())
    # print(Jack.bark())
    # print(Jack.sleep())
    # print(Jack.birthday())
    # Bruce = Cat("Bruce", 1, "Zakhar")
    # print(Bruce.run())
    # print(Bruce.jump())
    # print(Bruce.meow())
    # print(Bruce.sleep())
    # print(Bruce.birthday())
    # Cache = Parrot ("Cache", 1, "Zakhar")
    # print(Cache.run())
    # print(Cache.jump())
    # print(Cache.fly())
    # print(Cache.sleep())
    # print(Cache.birthday())























# Hometask_14_6
# Создать родительский класс Pet,
# содержащий все общие методы
# классов
# Dog, Cat, Parrot. Унаследовать Dog,
# Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые
# имеются у родительского класса.
# Создать объект каждого класса и
# вызвать все его методы.


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        return f"{self.name} can jump"

    def run(self):
        return f"{self.name} can run"

    def sleep(self):
        return f"{self.name} can sleep"

    def birthday(self):
        return self.age + 1


class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f"{self.name} can bark"

class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        return f"{self.name} can meow"

class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        return f"{self.name} can fly"

if __name__ == '__main__':
    Jack = Dog("Jack", 3, "Tom")
    print(Jack.name, Jack.age, Jack.master)
    print(Jack.run())
    print(Jack.jump())
    print(Jack.bark())
    print(Jack.sleep())
    print(Jack.birthday())
    print()
    Bruce = Cat("Bruce", 1, "Zakhar")
    print(Bruce.name, Bruce.age, Bruce.master)
    print(Bruce.run())
    print(Bruce.jump())
    print(Bruce.meow())
    print(Bruce.sleep())
    print(Bruce.birthday())
    print()
    Cache = Parrot("Cache", 2, "Tanya")
    print(Cache.name, Cache.age, Cache.master)
    print(Cache.run())
    print(Cache.jump())
    print(Cache.fly())
    print(Cache.sleep())
    print(Cache.birthday())