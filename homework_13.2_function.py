import random


# Hometask_13_4
# Напишите функцию, которая
# создает список случайных
# элементов. На фход функция
# принимает кол-во элементов,
# минимальное и максимальное
# значение
# In: rand_nums(7, 2, 12)
# Out: [12, 6, 9, 2, 11, 5, 8]


# # #1
# # def rand_nums(len_n, min_n, max_n):
# #     return [random.randint(min_n, max_n) for i in range(len_n)]
# # print(rand_nums(7, 2, 12))
# # #2
# rand_nums = lambda len_n, min_n, max_n: [random.randint(min_n, max_n) for i in range(len_n)]
# print(rand_nums(7, 2, 12))




# Hometask_13_5
# Преобразуйте задачу с покупкой
# торта из экзамена 2 в функцию.


# cake = {"наполеон": [["масло", "мука", "сахар"], 5, 1450],
#         "медовик": [["масло", "мука", "мед"], 6, 2451],
#         "киевский": [["масло", "мука", "сахар"], 5, 1360]}
# k_cake = input("Какой торт Вы хотели бы приобрести: ").lower()
# w_cake = input("Что Вы хотели бы уточнить: ").lower()
# def f_cake(kind_cake, wish):
#     for k,v in cake.items():
#         if kind_cake == k:
#             if wish == "описание":
#                 print(f"торт {k} састоит из {v[0]}")
#                 gr = int(input("Сколько торта Вам положить: "))
#                 print(f" к оплате {cake[k][1] * gr / 100}")
#                 print(f"торта {k} осталось {cake[k][-1] - gr} грамм")
#             elif wish == "цена":
#                 print(f"торт {k} стоит {v[1]} рубля")
#             elif wish == "количество":
#                 print(f"торта {k} осталось {v[-1]} грамм")
#
# f_cake(k_cake, w_cake)



# Hometask_13_6
# Напишите функцию,
# вычисляющую значение
# факториала числа N.
# Используйте рекурсию
# In: 5
# Out: 120


# n = int(input())
# def factorial(num):    #это я решал до просмотра видео
#     global mult
#     mult = 1
#     if num != 0:
#         factorial(num-1)
#         mult = num * mult
#     return mult
# print(factorial(n))

# def factorial(num):
#     if num == 1:
#         return 1
#     return factorial(num - 1) * num
# print(factorial(n))



# 13.11
# Напишите декоратор к функции
# деления, который меняет
# местами делимое и делитель
# In: div(2, 4)
# Out: 2.0


# def decor(f_div):
#     def iner(n1, n2):
#         f_div(n2, n1)
#     return iner
#
# @decor
# def div(num_1, num_2):
#     print(num_1/num_2)
#
# div(2, 4)


