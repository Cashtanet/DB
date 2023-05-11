# import sys
# print(sys.platform)
# print(2**100)
# x = 'Spam'
# print(x * 8)
#
# ''''#!/usr/local/bin/python'''  # в Unix системах в начале файла указывается путь к интерпретатору Python
# print('The Bright Side ' + 'of Life...')
#
#
# import my_file
#
# print(my_file.summa(10, 15))
# print(my_file.summa("Fuck ", "the system!"))
# print(my_file.summa([1, 2, 3], [4, 5, 6]))
# print(my_file.summa(40, 15))
#
# import three_names
#
# print(three_names.a)
#
# print(dir(three_names))
# import random

# exec(open('module .ру1').read()) #  является еще одним приемом
# # запуска файлов из интерактивной подсказки без импортирования и последующей перезагрузки.


# #
# a = [1, 2, 3]
# b = [1, 2, 3]
# s = []
# s.append(a)
# s.append(b)
# print(s)
# a.extend(b)
# print(a)


# s = [1, 2, 3, 4, 5, 6, 8, 6 , 6]
# print(tuple(s))

# print(len(str(2**1000)))


# print(3.1415 * 2)


# import random
# s = random.random()
# print(s)

# import random
# s = random.randrange(0,1000, 33)
# print(s)

# help(random.Random)


# j = 'sp\xc4\u00c4\U000000c4m'
# k = u'а\х01с'
# s = 'sp\xc4m'
# print(j)
# print(s, k)
# print(16**16)
# print(2**64)


# m = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]  #list comprehension (списочные(списковые) включения
# s1 = [row[1] for row in m]
# s2 = [row[1] + 1 for row in m]
# s3 = [row[1] for row in m if row[1] % 2 == 0]
# diag = [m[i][i] for i in [0, 1, 2]]
# doubles = [c * 2 for c in 'spam']
# a1 = list(range(-6, 7, 2))
# a2 = list(range(4))
# b1 = [[x ** 2, x ** 3] for x in range(4)]
# b2 = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
# c1 = list(map (sum, m)) #создание множества сумм элементов m
# c2 = {sum(row) for row in m}
# c3 = {i: sum(m[i]) for i in range(3)} #создание словаря эз сумм m
# c4 = [ord(x) for x in 'spaam']
# c5 = {ord(x) for x in 'spaam'} #множество без дубликатов
# c6 = {x: ord(x) for x in 'spaam'} #словарь с уникальными ключами
# c7 = (ord(x) for x in 'spaam') #генератор значений
# print(s1, s2, s3, diag, doubles)
# print(a1)
# print(a2)
# print(b1)
# print(b2)
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(c6)
# print(c7)


# s = [[1, 2], [3, 4]]
# s = dict(s)
# print(s)


# bob1 = dict(name='Bob', job='dev', age=40) # Ключевые слова
# bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Связывание вместе
# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
#        'jobs': ['dev', 'mgr'],
#        'age': 40.5}
# rec['jobs'].append('janitor')
# print(bob1)
# print(bob2)
# print(rec['name']['first'])
# print(rec['jobs'][-1])
# print(rec)


a = 550
b = 1250
print(a * b)
print(b//a)