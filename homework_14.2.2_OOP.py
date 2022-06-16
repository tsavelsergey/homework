# 14.11
# Установите статичечкий атрибут
# мин цена в салоне красоты
# Допишите методы.
# Маникюр стоит на 20% больше
# Стрижка зависит от длины
# волос:
# меньше 30см - +20%,
# От 30 до 50 см - +50%
# Свыше 50 см - +80%




class BeautySalon:

    min_price = 10

    def manic(self):
        return self.min_price + self.min_price * 0.2

    def haircut(self, find_hair):
        if 0 < find_hair < 30:
            return self.min_price + self.min_price * 0.2
        elif 30 <= find_hair < 50:
            return self.min_price + self.min_price * 0.5
        elif find_hair >= 50:
            return self.min_price + self.min_price * 0.8
        else:
            return f"Enter the correct hair length"

if __name__ in "__main__":
    Woman = BeautySalon()
    print(Woman.min_price)
    print(Woman.manic())
    print(Woman.haircut(-20))
    print(Woman.haircut(20))
    print(Woman.haircut(80))





# class Building:
#     def __init__(self, floor, windows, doors):
#         self.floor = floor
#         self.windows = windows
#         self.doors = doors
#
#     def build(self):
#         print(f'The house was built')
#
#     def populate(self):
#         print(f'The house was populated')
#
#     def demolish(self):
#         print(f'The house was demolished')
#
#
# class BeautySalonMixin:
#     def manic(self):
#         pass
#
#     def haircut(self):
#         pass
#
#     def salon_opening_hours(self, time):
#         if self.open_close> time > self.open_time:
#             return "салон открыт"
#         return "салон закрыт"
#
#     def set_timework(self, timeopen, timeclose):
#         self.open_time = timeopen
#         self.open_close = timeclose
#
#
# class HouseWithSalon(Building, BeautySalonMixin):
#     def __init__(self, floor, windows, doors):
#         super().__init__(floor, windows, doors)
#         self.open_time = None
#         self.close_time = None
#
#
# if __name__ == "__main__":
#     hws = HouseWithSalon(2, 2, 2)
#     hws.set_timework(10, 22)
#     print(hws.salon_opening_hours(13))
#     print(hws.salon_opening_hours(23))
#     print(hws.open_close)