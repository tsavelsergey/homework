



# 2_1
# Дан список чисел.
# Выведите те его элементы,
# которые встречаются в списке
# только один раз.
# Элементы нужно выводить в
# том порядке, в котором они
# встречаются в списке.

# ls = [int(i) for i in input().split()]
#
# for i in ls:
#     if ls.count(i) == 1:
#         print(i)

# 2_2
# Дан список символов.
# Посчитайте сколько в нем пар
# элементов, равных друг другу
# (одинаковых).
# Считается, что любые два
# элемента, равные друг другу,
# образуют одну пару, которую
# необходимо посчитать.

# ls = [int(s) for s in input().split()]
# counter = 0
# for i in range(len(ls)):
#     for j in range(i + 1, len(ls)):
#         if ls[i] == ls[j]:
#             counter += 1
# print(counter)




# 2_3
# Даны 2 кортежа:
# c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# Необходимо определить:
# 1. Сумма элементов какого из
# кортежей больше
# 2. Порядковые номера
# минимальных и максимальных
# элементов этих кортежей.


# c_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# c_2 = (45, 21,124,76,5,23,91,234)
# if sum(c_1) > sum(c_2):
#     print(f" Сумма больше в кортеже {c_1}")
# else:
#     print(f" Сумма больше в кортеже {c_2}")
# print(f"В кортеже с_1 минимальный элемент {c_1.index(min(c_1))}, максимальный элемент {c_1.index(max(c_1))}")
# print(f"В кортеже с_2 минимальный элемент {c_2.index(min(c_2))}, максимальный элемент {c_2.index(max(c_2))}")


#
# 2_4
# Дана строка: ' An apple a day
# keeps the doctor away'
# Создайте из нее словарь:
# ключи – элементы строки,
# значения – количество
# вхождений данного элемента
# в строку.

# str = " An apple a day keeps the doctor away"
# dic = {i: str.count(i) for i in str}
# print(dic)


# 2_5
# Клиент приходит в кондитерскую.
# Реализуйте кондитерскую:
# 1. Если клиент хочет посмотреть
# описание – название и состав
# 2. Цену – название и стоимость
# 3. Количество – название и
# сколько осталось.
# 4. Купить – стоимость покупки и
# остаток в кондитерской.
# Словарь: ключи – название
# продукции, значения – описание,
# стоимость, количество.


# Какой торт Вы хотели бы приобрести: наполеон
# >> Что Вы хотели бы уточнить: описание
# >> Торт наполеон состоит из масло мука сахар
# >> Сколько торта Вам положить: 200

# import pyttsx3
#
#
# engine = pyttsx3.init()
# engine.setProperty("rate", 799)
# engine.setProperty("volume", 0.9)
#
# cake = {"наполеон": [["масло", "мука", "сахар"], 5, 1450],
#         "медовик": [["масло", "мука", "мед"], 6, 2451],
#         "киевский": [["масло", "мука", "сахар"], 5, 1360]}
#
# engine.say("Какой торт Вы хотели бы приобрести")
# engine.runAndWait()
#
#
# kind_cake = input("Какой торт Вы хотели бы приобрести: ").lower()
#
# engine.say("Что Вы хотели бы уточнить")
# engine.runAndWait()
# wish = input("Что Вы хотели бы уточнить: ").lower()
#
# for k,v in cake.items():
#     if kind_cake == k:
#         if wish == "описание":
#                 engine.say("Что Вы хотели бы уточнить")
#                 engine.runAndWait()
#             print(f"торт {k} састоит из {v[0]}")
#             gr = int(input("Сколько торта Вам положить: "))
#             print(f" к оплате {cake[k][1] * gr / 100}")
#             print(f"торта {k} осталось {cake[k][-1] - gr} грамм")
#         elif wish == "цена":
#             print(f"торт {k} стоит {v[1]} рубля")
#         elif wish == "количество":
#             print(f"торта {k} осталось {v[-1]} грамм")

# 2_6
# Даны 2 списка чисел. В них
# могут быть одинаковые числа.
# Посчитайте, сколько в списках
# одинаковых чисел.

# ls_1 = [int(i) for i in input().split()]
# ls_2 = [int(i) for i in input().split()]
#
# c = set(ls_1) & set(ls_2)
# print(len(c))


# s = 0
# if len(ls_1) > len(ls_2):
#     for i in ls_1:
#         if i in ls_2:
#             s += 1
# else:
#     for i in ls_2:
#         if i in ls_1:
#             s += 1
# print(s)

# ls1 = input().split()
# ls2 = input().split()
# set1 = set(ls1)
# set2 = set(ls2)
# uniq = set1 & set2
# print(len(uniq))


# 2_7
# Напишите программу,
# демонстрирующую работу
# try
# \except
# \finally
# .


# try:
#     dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#     for key in list(dic.keys()):
#         if key % 2 != 0:
#             print(key)
# except NameError:
#     print("Создать словарь, ключи — числа, значения — слова.")
# finally:
#     print("dic")



# 2_8
# В текстовый файл построчно
# записаны фамилия, имя
# учащихся класса и его оценка
# за тест.
# Вывести на экран всех
# учащихся, чья оценка меньше
# 3 баллов и посчитать средний
# балл по классу.


# with open("text.txt", "r") as f:
#     bal = 0
#     amount = 0
#     for line in f:
#         line = line.rstrip()
#         s = int(line[-1])
#         bal += s
#         amount += 1
#         if s < 3:
#             print(line)
# print("Средняя оценка за тест =", bal / amount)