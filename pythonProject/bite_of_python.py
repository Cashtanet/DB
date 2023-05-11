
# print("{0:_^11}".format("hello")) #?????????????

###
# i = 5
# print(i)
# i = i + 1
# print(i)
#
# s = '''Это многострочная строка.
# Это вторая её строчка.'''
# print(s)

### логический конец строки ";"
# i = 5; print(i)


# s = '''Это многострочная строка. \
# Это вторая её строчка.'''
# print(s)


# print(list("Ghbdtn")) #!!!!!!!

# s = "sdfsdsdgsdgg"
# # lis = []
# # for i in s:
# #     lis.append(i)
# print(lis)


# print([i**2 for i in range(5)])



#
# def func_outer():
#     x = 2
#     print(x)
#
#     def func_inner():
#         nonlocal x
#         x = 5
#
#     func_inner()
#     print(x)
#
# func_outer()




# def total(a = 5, *numbers, **phonebook):
#     print('a', a)
#
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560, Sam=5561))



# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
# n = int(input())
# total(10, 1, 2, 3, extra_number=n)



# def some_function():
#     pass
#
# print(some_function())




# def print_max(x, y):
#     '''Выводит максимальное из двух чисел.
#
#     Оба значения должны быть целыми числами'''
#     x = int(x)
#     y = int(y)
#
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
#
# print_max(3, 5)
# print(print_max.__doc__)  #печать документации


# def nth_even(n):
#     s = []
#     for i in range(0,n + 2,2):
#         s.append(i)
#     return s[-1]
#
# nth_even(5)



# # 'ab' - сокращение от 'a'ddress'b'ook
# ab = { 'Swaroop' : 'swaroop@swaroopch.com',
# 'Larry' : 'larry@wall.org',
# 'Matsumoto' : 'matz@ruby-lang.org',
# 'Spammer' : 'spammer@hotmail.com'
# }
# print("Адрес Swaroop'а:", ab['Swaroop'])
# # Удаление пары ключ-значение
# del ab['Spammer']
# print('\nВ адресной книге {0} контакта\n'.format(len(ab)))
# for name, address in ab.items():
#     print('Контакт {0} с адресом {1}'.format(name, address))
# # Добавление пары ключ-значение
# ab['Guido'] = 'guido@python.org'
# if 'Guido' in ab:
#     print("\nАдрес Guido:", ab['Guido'])


# a = set(["ab", "bc", "cd", "de"])  #пересечение множеств
# b = set(["ag", "cd", "de", "qr"])
# s = a.intersection(b)  #пересечение множеств
# print(s)


# print('Простое присваивание')
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!
# del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка
# print('shoplist:', shoplist)
# print('mylist:', mylist)
# # Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# # без пункта "яблоко", подтверждая тем самым, что они указывают на один
# # объект.
# print('Копирование при помощи полной вырезки')
# mylist = shoplist[:] # создаём копию путём полной вырезки
# del mylist[0] # удаляем первый элемент
# print('shoplist:', shoplist)
# print('mylist:', mylist)
# # Обратите внимание, что теперь списки разные




# import os
# import time
# # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = ['"C:\\My Documents"', 'C:\\Code']
# # Заметьте, что для имён, содержащих пробелы, необходимо использовать
# # двойные кавычки внутри строки.
# # 2. Резервные копии должны храниться в основном каталоге резерва.
# target_dir = 'E:\\Backup' # Подставьте ваш путь.
# # 3. Файлы помещаются в zip-архив.
# # 4. Именем для zip-архива служит текущая дата и время.
# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# # 5. Используем команду "zip" для помещения файлов в zip-архив
# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# # Запускаем создание резервной копии
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')



# class Person:
#     pass # Пустой блок
# p = Person()
# print(p)


# class Person:
#     def sayHi(self):
#         print('Привет! Как дела?')
# p = Person()
# p.sayHi()
# Этот короткий пример можно также записать как Person().sayHi()



# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print('Привет! Меня зовут', self.name)
#
# p = Person('Alex')
# p.say_hi()
# # Предыдущие 2 строки можно
# # Person('Swaroop').say_hi()


# 111 перечитать!



# class Robot:
#         '''Представляет робота с именем.'''
#         # Переменная класса, содержащая количество роботов
#         population = 0
#         def __init__(self, name):
#         #'''Инициализация данных.'''
#             self.name = name
#             print('(Инициализация {0})'.format(self.name))
#         # При создании этой личности, робот добавляется
#         # к переменной 'population'
#         Robot.population += 1
#     def __del__(self):
#         '''Я умираю.'''
#         print('{0} уничтожается!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#     def sayHi(self):
#     '''Приветствие робота.
#     Да, они это могут.'''
#         print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
#     def howMany():
#     '''Выводит численность роботов.'''
#         print('У нас {0:d} роботов.'.format(Robot.population))
#     howMany = staticmethod(howMany)
# droid1 = Robot('R2-D2')
# droid1.sayHi()
# Robot.howMany()
# droid2 = Robot('C-3PO')
# droid2.sayHi()
# Robot.howMany()
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу. Давайте уничтожим их.")
# del droid1
# del droid2
# Robot.howMany()




# poem = '''\
# Программировать весело.
# Если работа скучна,
# Чтобы придать ей весёлый тон -
# используй Python!
# '''
# f = open('poem.txt', 'w') # открываем для записи (writing)
# f.write(poem) # записываем текст в файл
# f.close() # закрываем файл
# f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
# # режим чтения ('r'eading)
# while True:
#     line = f.readline()
#     if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
#         break
#     print(line, end='')
# f.close() # закрываем файл



# import pickle
# # имя файла, в котором мы сохраним объект
# shoplistfile = 'shoplist.data'
# # список покупок
# shoplist = ['яблоки', 'манго', 'морковь']
# # Запись в файл
# f = open(shoplistfile, 'wb')
# pickle.dump(shoplist, f) # помещаем объект в файл
# f.close()
# del shoplist  # уничтожаем переменную shoplist
# # Считываем из хранилища
# f = open(shoplistfile, 'rb')
# storedlist = pickle.load(f) # загружаем объект из файла
# print(storedlist)


# import sys, warnings
# print(sys.version_info)


# import os, platform, logging
# if platform.platform().startswith('Windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
#     os.getenv('HOMEPATH'), \
#     'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
#     print("Сохраняем лог в", logging_file)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename = logging_file,
#     filemode = 'w',
#     )
# logging.debug("Начало программы")
# logging.info("Какие-то действия")
# logging.warning("Программа умирает")


