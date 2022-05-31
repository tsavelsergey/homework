
# С клавиатуры вводится
# 7мизначное число.
# Если четных цифр в нем
# больше, чем нечетных, то
# найти сумму всех цифр.
# Если нечетных больше, чем
# четных, то найти
# произведение 1, 3 и 6 цифр.

# num = int(input())
# n = num
# even = 0
# odd = 0
# ls = []
#
# while num != 0:
#     last = num % 10
#     ls.append(last)
#     if last % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     num = num // 10
# if even > odd:
#     print("Четных цифр больше, сумма цифр числа = ", sum(ls))
# else:
#     n = str(n)
#     print(f"Нечетных цифр больше, произведение, {int(n[0])}, {int(n[2])} и {int(n[5])} = {int(n[0]) * int(n[2]) * int(n[5])}")


# number = int(input())
# odd = 0
# even = 0
# summ = 0
# iter = 1
# mult = 1
#
# while number != 0:
#     last = number % 10
#     if last % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
#     summ += last
#     number = number // 10
#
#     if iter == 2 or iter == 5 or iter == 7:
#         mult *= last
#     iter += 1
#
# if odd > even:
#     print(mult)
# elif even > odd:
#     print(summ)



# С клавиатуры вводится строка.
# Если количество согласных и
# гласных в ней одинаково, то
# выведите на экран все гласные
# буквы

# word = input().lower()
# vowels = "iuyoea"
# vow = 0
# con = 0
# str1 = ""
# for i in word:
#     if i in vowels:
#         vow += 1
#         str1 += i
#     elif i.isalpha() and i not in vowels:
#         con += 1
# if vow == con:
#     print(str1)



# С клавиатуры вводятся 2 числа a и b и генеруется 2 числа
# рандомно r1 и r2. Все числа от 1 до 20. Посчитать сколько раз a > r1
# and b > r2. Проверку выполнить 6 раз. В случае равенства
# (когда a, b больше 3 раза и r1, r2 больше 3 раза) вывести на
# печать рандомные числа, полученные в 4 итерации.

# import random
#
#
# iter_4_1 = ""
# iter_4_2 = ""
# ab_more = 0
# r_more = 0
# for i in range(6):
#     iter = i+1
#     a = int(input("Введите первое число:"))
#     b = int(input("Введите второе число:"))
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     if a > r1 and b > r2:
#         ab_more += 1
#     else:
#     # elif a < r1 and b < r2:
#         r_more += 1
#     if iter == 4:
#         iter_4_1 = r1
#         iter_4_2 = r2
#         # print(f"Рандомные числа, полученные в 4ой итерации: {iter_4_1}, {iter_4_2}")
# if ab_more == r_more:
#     print(f"Рандомные числа, полученные в 4ой итерации: {iter_4_1}, {iter_4_2}")


# Посчитать сколько раз
# встречается искомая цифра в
# рандомных числах от 1 до 20.
# Количество рандомных чисел и
# искомая цифра задаются с
# клавиатуры.

# import random
#
#
# goal = int(input("Какую цифру будем искать:"))
# count = int(input("Сколько раз будем искать эту цифру:"))
# iter = 1
# c = 0
# while iter <= count:
#     r1 = random.randint(1, 20)
#     print("r1", r1)
#     while r1 != 0:
#         if r1 % 10 == goal:
#             c += 1
#         r1 = r1 // 10
#     iter += 1
# print(f" Цифра {goal} встретилась {c} раз")

# Вводится строка, содержащая
# буквы, цифры, пробелы и
# прочие символы.
# Выведите на печать все цифры.
# Гарантируется, что цифры
# будут только положительные.

# str_1 = input()
# for i in str_1:
#     if i.isdigit():
#         print(i)


# Вводится строка, содержащая
# буквы, цифры, пробелы и
# прочие символы.
# Посчитайте:
# - Сколько пар букв (стоят
# рядом) верхнего регистра
# - Сколько пар букв (стоят
# рядом) нижнего регистра
# - Сколько согласных букв
# - Сколько гласных букв
# - Сколько всего букв


# text = input()
# vowels = "eyuioa"
# vow = 0
# consonants = 0
# letters = 0              # можно посчитать сложив гласные и согласные
# upper_case = 0
# lower_case = 0
#
# for i in text.lower():
#     if i.isalpha():
#         letters += 1
#         if i in vowels:
#             vow += 1
#         else:
#             consonants += 1
#
# for i in range(1, len(text)):
#     if text[i-1].isupper() and text[i].isupper():
#         upper_case += 1
#     elif text[i-1].islower() and text[i].islower():
#         lower_case += 1
#
# print("Пар верхнего регистра", upper_case)
# print("Пар нижнего регистра", lower_case)
# print("Гласных букв", vow)
# print("Согласных букв", consonants)
# print("Всего букв", letters)            # можно посчитать сложив гласные и согласные


