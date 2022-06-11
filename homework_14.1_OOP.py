

# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре
# атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все
# методы
# объекта и вывести на экран все его
# атрибуты.
#
# class Dog:
#
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
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
# if __name__ == '__main__':
#     Jack = Dog(78, 30, "Jack", 3)
#     print(Jack.height, Jack.weight, Jack.name, Jack.age)
#     print(Jack.run())
#     print(Jack.jump())
#     print(Jack.bark())
#     Bobik = Dog(60, 20, "Bobik", 1)
#     print(Bobik.height, Bobik.weight, Bobik.name, Bobik.age)
#     print(Bobik.run(), Bobik.jump(), Bobik.bark(), sep=", ")




# Hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод
# принимает на вход новое имя и меняет
# атрибут имени у
# объекта. Создать один объект класса.
# Вывести имя.
# Вызвать метод change_name. Вывести имя.



class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return f"Dog can jump"

    def run(self):
        return f"Dog can run"

    def bark(self):
        return f"Dog can bark"

    def change_name(self, new_name):
        n = self.name
        self.name = new_name
        return f"{n} has a new nickname {self.name}" # Если понадобится вывести сообщение о смене клички

if __name__ == '__main__':
    Jack = Dog(78, 30, "Jack", 3)
    print(Jack.name)
    n_name = input("enter a new nickname ")
    Jack.change_name(n_name)
    print(Jack.name)
