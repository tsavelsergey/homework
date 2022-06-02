
# Hometask_13_1
# Из полученного списка чисел
# создайте список с суммами
# этих чисел, отсортированными
# по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]

# ls = [int(i) for i in input().split()]
# ls_nums = []
# #-------------------------------
# # for num in ls:  # Var 1
# #     sum_n = 0
# #     while num != 0:
# #         last = num % 10
# #         sum_n += last
# #         num = num // 10
# #     ls_nums.append(sum_n)
# # print(sorted(ls_nums))
#
# #-------------------------------
#
# def sum_num(num):  # Var 2
#     sum_n = 0
#     while num != 0:
#         last = num % 10
#         sum_n += last
#         num = num // 10
#     return sum_n
# for n in ls:
#     ls_nums.append(sum_num(n))
# print(sorted(ls_nums))


# Hometask_13_2
# Напишите функцию f(x), которая
# возвращает значение следующей
# функции, определённой на всей
# числовой прямой:
# In: 4.5
# Out: 7.25


# num = float(input())
# def f(x):
#     if x <= -2:
#         return 1-(x+2)**2
#     elif -2 < x <= 2:
#         return -x/2
#     elif 2 < x:
#         return (x-2)**2+1
# print(f(num))


# Hometask_13_3
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
# In: 852 85 784 58
# Out: [852, 784, 58]


# ls = [int(i) for i in input().split()]
# def nums(list_nums):
#     ls_2 = []
#     for i in list_nums:
#         if i % 2 == 0:
#             ls_2.append(int(i/2))
#     return ls_2
# print(nums(ls))