#
# Решить задачу с обработкой исключений.
# Вызвать ошибку KeyError и вернуть
# программу к исполнению команд. Укажите
# пользователю какие страны он может
# выбрать.


# Создать словарь, который в качестве ключа будет использовать страну, а в качестве
# значения - ее столицу. Внеси в него следующие страны: Россия (Москва), Украина
# (Киев), Италия (Рим), Испания (Мадрид), Болгария (София).
# Программа должна запрашивать у пользователя, столицу какой страны он хочет узнать
# и выдавать результат.


# dic = {"Россия": "Москва", "Украина": "Киев", "Италия": "Рим", "Испания": "Мадрид", "Болгария": "София"}
# country = input("Введите страну которой столицу вы хотите узнать ")
# try:
#     print(dic[country])
# except KeyError:
#     print(f" выберите страну из списка {dic.keys()}")




# Решить задачу с обработкой исключений.
# Вызвать ошибку ValueError и сообщить,
# что б пользователь ввел число:

# Определите кол-во отрицательных и положительных элементов последовательности,
# заканчивающейся числом 0.

# try:
#     num = int(input("Enter a num "))
#     positive_number = []
#     negative_number = []
#     while num != 0:
#         if num >= 0:
#             positive_number.append(num)
#         elif num < 0:
#             negative_number.append(num)
#         num = int(input("Enter a num "))
#     print("number of positive numbers = ", len(positive_number))
#     print("number of negative numbers = ", len(negative_number))
# except ValueError:
#     print("Enter a number")



# Решить задачу с обработкой исключений.
# Вызвать ошибку NameError и сообщить,
# что необходимо создать словарь в котором ключи числа

 # Создать словарь, ключи — числа, значения — слова. Удалить из него все
# пары с нечетными ключами. Вывести на печать
# В этом вам может помочь статья, что сбрасывала ранее.

# try:
#     dic = {1: 'one', gg: 'two', 3: 'three', 4: 'four', 5: 'five'}
#     for key in list(dic.keys()):
#         if key % 2 != 0:
#             del dic[key]
#     print(dic)
# except NameError:
#     print("Создать словарь, ключи — числа, значения — слова.")