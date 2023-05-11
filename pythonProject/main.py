# # num1 = int(input ("Введите первое число: "))
# # num2 = int(input ("Введите второе число: "))
# # print("Результат: ",num1 + num2)
# # print("Результат: ",num1 - num2)
# # print("Результат: ",num1 / num2)
# # print("Результат: ",num1 * num2)
# # print("Результат: ",num1 ** num2)
# # print("Результат: ",num1 // num2)
# # print("Результат: ",num1 % num2)
# #
# #
# # # УСЛОВНЫЕ ОПЕРАТОРЫ
# # #
# # user_data = int(input("Введите число: "))
# # #
# # if user_data > 5:
# #     print("Number is bigger than 5")
# # elif user_data == 5:
# #     print("Number is equal 5")
# # else:
# #     print("Number is smaller than 5")
# # #
# # isHappy = True
# #
# # if isHappy:
# #     print("User is happy")
# # else:
# #     print("User is unhappy")
# #
# # data = input()
# #
# # number = 5 if data == "Five" else 0
# #
# # # if data == "Five":
# # #     number = 5
# # # else:
# # #     number = 0
# # print(number)
# #
# #
# # ЦИКЛЫ
# #
# for i in range(5, 125, 5):
#     print(i)
# #
# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#        count += 1
# print("Count:", count)
# #
# # i = 5
# # while i <= 15:
# #     print(i)
# #     i += 2
# #
# # for i in range(1, 11):
# #     if i == 5:
# #         break
# #     if i%2 == 0:
# #         continue
# #     print(i)
# #
# #
# # ЦИКЛЫ С УСЛОВИЯМИ
# #
# # found = None
# # for i in "Hello":
# #     if i == "e":
# #         found = True
# #         break
# # else:
# #     found = False
# # print(found)
# #
# # СПИСКИ (МАССИВЫ)
# #
# # nums = [5, 7, 2, 3, 10, 10.5, 1.595, "Hello", True, [10.5, 13, 852]]
# #
# # nums[0] = 50
# # nums[8] = 1
# #
# # print(nums[-1][2])
# #
# # numbers = [0.5, 10, 2, 10, False, 7]
# # numbers.append(100)
# # numbers.append(True)
# # numbers.insert(3, 10)
# # numbers.extend([5, 6, 13])
# # numbers.sort()#
# # numbers.reverse()
# # numbers.pop(-2)
# # numbers.remove(True)
# # numbers.clear()
# # print(len(numbers))
# #
# # nums = [5, 2, 7, "50", False]
# #
# # for el in nums:
# #     el *= 2
# #     print(el)
# #
# #
# #
# # n = int(input("Enter length: "))
# # user_list = []
# #
# # i = 0
# # while i < n:
# #     string = "Enter element #"+ str(i+1)+ ": "
# #     user_list.append(input(string))
# #     i += 1
# #
# # print(user_list)
# #
# # lis = [255, 5, 8, -4.5, 10, 9, 0, -0.2, 52]
# # print(lis[1:5:2])
# #
# # # a = input("Enter your name: ")
# # # word = "itproger"
# # word = "Football, basketball, skate"
# # # print(word.capitalize())
# # # print(word.find('p'))
# hobby = word.split(', ')
# print(hobby[1])
# # #
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
# print(hobby)
# #
# # result = ", ".join(hobby)
# # print(result)
# #
# #
# # word = 'Football'
# # print(word[1:-1:2])
# #
# #
# # list = [324,152,1253,1254,5,6,7,8,9]
# #
# # # for i in range(len(list)):
# # #     print(list[i])
# # print(*list, sep= ",")
# #
# # lis = [6,4,"Stroka", True, 6.5, 14,15,645,'Male']
# # print(lis[::-1])
# #
# #
# #
# # КОРТЕЖИ (НЕИЗМЕНЯЕМЫЕ СПИСКИ)(занимают меньше памяти)
# # используются для передачи данных пользователю
# #
# # data = (4,6,7,3,6,True,5.6,'Hello')
# # # data[3] = 1 нельзя
# # # print(data[1:5:])
# # # print(data.count(4))
# # # print(len(data))
# # print(data)
# #
# # for el in data:
# #     print(el)
#
#
# # import sys
# # var1="Python"
# # var2='Hello world'
# # var3=1000000000000000000000000000000000000000000
# # print(sys.getsizeof(var1))
# # print(sys.getsizeof(var2))
# # print(sys.getsizeof(var3)
#
# # СЛОВАРИ
#
# # country = {'code': 'RU','name': 'Russian', 'population': 144}
# # country = dict(code='RU', name='Russian') # аналогично
# # print(country['name'])
#
# # for key, value in country.items():
# #     print(key, ' - ', value)
#
# # print(country.get('name')) одинаково print(country['name'])
# # country.clear()
# # country.pop('name') #удаление элемента по ключу
# # country['code'] = 'None' #change a value === country.update('code')
# # print(country.keys()) #print only keys
# # print(country.values()) #print only values
# # print(country.items()) #print tuples  of elements
#
# # person = {
# #     'user_1': {
# #         'first_name': 'John',
# #         'last-name': 'Marley',
# #         'age': 45,
# #         'address': ['г.Москва', 'ул. Ленина', 'д.45'],
# #         'grades': {'math': 5, 'physics': 3}
# #     },
# #     'user_2': {
# #
# #     }
# # }
# # print(person['user_1']['address'][1])
#
#
#
# # МНОЖЕСТВА ЭТО СПИСОК, БЕЗ ПОВТОРЯБЩИХСЯ ЭЛЕМЕНТОВ (ЭЛЕМЕНТЫ В СЛУЧАЙНОМ ПОРЯДКЕ)
# # МОЖНО СРАЗУ УДАЛИТЬ ПОВТОРЯЮЩИЕСЯ ЭЛЕМЕНТЫ СПИСКА СДЕЛАВ ЕГО МНОЖЕСТВОМ
#
# # data = set('Hello')
# # data = {5,7,4,3,5} #без ключей это множество. с ключами - словарь
# #
# # data.add(32) # добавление элемента
# # data.update(['32',64,128])#добавление нескольких элементов
# # data.remove(4)#удаление элемента со значением
# # data.pop()# delete firts el
# # data.clear()#clear the set
#
# # print(data)
#
#
# # nums = [5, 7, 3, 5, 5]
# # new_nums = set(nums)
# #
# # print(new_nums)
#
# #
# # new_data = frozenset([5, 7, 4, 3, 5]) #НЕИЗМЕНЯЕМОЕ МНОЖЕСТВО (КОРТЕЖ)
# #
# # print(new_data)
#
#
#
#
# #ФУНКЦИИ (ПОДПРОГРАММА)
#
#
# # def test_func():
# #     print('Hello', end='')
# #     print('!')
#
# # test_func()
# # test_func()
# # test_func()
#
# # def test_func(word):
# #     print(word, end='')
# #     print('!')
# #
# #
# # test_func('Hi')
# # test_func('Hello')
# # test_func(5)
#
#
# # def summa(a, b):
# #     res = a + b
# #     print('Result: ', res)
# #
# # res = summa(5,7)
# # print(res)
# # summa('H', 'i')
#
#
# # def summa(a, b):
# #     res = a + b
# #     return res
# #
# # res = summa(5.5,7.5)
# # print(res)
# # # summa('H', 'i')
#
#
# # def summa(a, b):
# #     return a + b
# #
# # res = summa(5.5,7.5)
# # print(res)
# # print(summa('H', 'i'))
#
#
#
# # nums1 = [5, 7, 9, 4, 2, 1, -10] #searching for min elevent in list
# # min = nums1[0]
# # for el in nums1:
# #     if el < min:
# #         min = el
# #
# # print(min)
# #
# #
# # nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2] #searching for min elevent in list
# #
# # min2 = nums2[0]
# # for el in nums2:
# #     if el < min2:
# #         min2 = el
# #
# # print(min2)
#
#
#
# # def minimal(l):
# #     min_number = l[0]
# #     for el in l:
# #         if el < min_number:
# #             min_number = el
# #     print(min_number)
# #
# # nums1 = [5, 7, 9, 4, 2, 1, -10]
# # minimal(nums1)
# #
# # nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
# # minimal(nums2)
# #
# # nums3 = [0.454, 0.345, 0.12, 0.134]
# # minimal(nums3)
#
#
# # def minimal(l):
# #     min_number = l[0]
# #     for el in l:
# #         if el < min_number:
# #             min_number = el
# #     return min_number
# #
# # nums1 = [5, 7, 9, 4, 2, 1, -10]
# # min1 = minimal(nums1)
# #
# # nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
# # min2 = minimal(nums2)
# #
# # nums3 = [0.454, 0.345, 0.12, 0.134]
# # min3 = minimal(nums3)
# #
# # sum = min1 + min2 + min3
# #
# # print(sum)
#
#
# # АНОНИМНЫЕ ФУНКЦИИ LAMBDA
#
# # func = lambda x, y: x * y #в одну строку(очень маленькие функции)
# #
# # res = func(5, 2)
# # print(res)
#
#
# # РАБОТА С ФАЙЛАМИ (ФАЙЛЫ ПОСЛЕ РАБОТЫ С НИМИ ДОЛЖНЫ БЫТЬ ЗАКРЫТЫ)
#
#
#
# # file = open('data/text.txt', 'w')# rewrite data in file
# # # file = open('data/text.txt', 'a')#add data (append)
# #
# # file.write('Hello\n')
# # file.write('!!!')
# #
# #
# # file.close()
#
#
# # data = input('Введите текст: ')
# # # file = open('data/text.txt', 'w')# rewrite data in file
# # file = open('data/text.txt', 'w')#add data (append)
# # file.write(data + "\n")
# #
# # file.close()
#
# #
# # file = open('data/text.txt', 'r')#reading file
# # # print(file.read())
# #
# # for line in file:
# #     print(line, end = '') end чтобы не было лишнего переноса строки
# #
# # file.close()
#
#
#
# # ОБРАБОТЧИК ИСКЛЮЧЕНИЙ
#
# # x = int(input("Введите число: "))
# # x += 5
# # print(x)
#
# # try:
# #     x = int(input("Введите число: "))
# #     x += 5
# #     print(x)
# # except ValueError:
# #     print("Мы же просили число!")
#
#
# # x = 0
# # while x == 0:
# #     try:
# #         x = int(input("Введите число: "))
# #         x += 5
# #         print(x)
# #     except ValueError:
# #         print("Мы же просили число!")
#
# # try:
# #     x = 5/1
# #     x = int(input())
# # except ZeroDivisionError: #ошибка деления на 0
# #     print("Деление на 0")
# # except ValueError: #ошибка типа данных
# #     print('Вы ввели то-то не так')
# # else:
# #     print("else")  # сработает если выполнился блок try без исключений
# # finally:   #этот блок сработает в любом случае (например закрыть файл)
# #     print("Finally")
#
#
#
#
# # МЕНЕДЖЕР WITH ..... AS
#
#
# # file = open('text.txt', 'r') #режим r(read) не
# #                               # позволяет создать новый файл
# # file.read()
# # file.close
#
#
# # try:
# #     file = open('text.txt', 'r')
# #     file.read()
# #     file.close()
# # except FileNotFoundError:
# #     print("Файл не найден")
# # finally:
# #     file.close() # ошибка(файл не определен)
#
# #
# # try:
# #     with open('text.txt', 'r', encoding="utf-8") as file: #with as открывает и самостоятельно закрывает файл
# #         print(file.read())
# # except FileNotFoundError:
# #     print("Файл не найден")
#
#
#
#
# # МОДУЛИ ПИТОН И РАБОТА С НИМИ
#
# # import time
# #
# # time.sleep(3) #заморозить прогу на 3 секунды
# # print("Hello")
#
#
# # import datetime as d #даем короткое имя модулю для упрощения
# #                     #этот модуль позволяется работать с текущей датой и временем)
# # print(d.datetime.now().time())
#
#
#
# # import datetime as d, sys, os, platform
# #
# # print(sys.path) #путь к текущему файлу проекта
# # print(os.name) #имя ос
# # print(platform.system()) #название системы
#
# import random
# import array
# import math
#
# import mymodule as my
#
# # from math import sqrt as s, ceil
# # # print(ceil(s(4))) #ceil округление
# #
# #
# #
# # print(my.name)
# # my.hello()
#
#
# # from mymodule import add_three_numbers as add
# # print(add(5, 10, 1))
#
#
# # import cowsay as c
# # c.cow("hello")
#
#
#
#
# # ООП
#
# # Функция вне класса =  метод внутри класса(одно и то же, называются по разному)
#
# # Объект – это кусок кода, описывающий элемент с конкретным набором характеристик и функций. Например, вы делаете видеоигру, в которой есть персонаж. Ваш герой.
# # Методы.Методы – это функции, описанные внутри объекта или класса. Они относятся к конкретному объекту и позволяют взаимодействовать с ними или другими частями
# # кода. Выше мы уже затронули «способности» персонажа-объекта, вот они и являются наиболее понятным описанием методов. Когда ваш персонаж выполняет действие
# # в игре, он задействует метод, описанный в его объекте.
# # Атрибуты. Атрибуты – это конкретные характеристики объекта. Если вы хоть немного знакомы с программированием, то атрибуты можно представить в виде переменных
# # с данными. Вернувшись к примеру с игровым персонажем, в качестве атрибутов можно представить характеристики в духе уровня выносливости, скорости и других
# # статических показателей.
# # Классы. Это наиболее абстрактная и обобщенная форма в ООП. Что-то в духе шаблона, на базе которого строятся другие элементы структуры кода.
# # Снова поясню на примере игры. В какой-нибудь онлайн-РПГ может быть куча разных героев: воины, лучники, люди, орки. Описывать каждого по отдельности
# # сложно и нецелесообразно, ведь у них много общих характеристик и методов.
# # Поэтому мы можем создать класс – то есть объект, способный стать базой для других объектов. Например, класс – персонаж. Он умеет ходить, драться,
# # имеет характеристики наподобие уровня здоровья или количества маны, то есть атрибуты, что есть у любых рас и классов в нашей РПГ. А уже человек-воин (объект)
# # с ником Nagibator777 будет содержать более специфичные характеристики и методы, зависящие от решений игрока и других внешних факторов. Класс – это пример
# # абстракции и наследования, упрощающий генерацию новых объектов.
# #
#
#
#
# # class Cat:
# #     name = None
# #     age = None
# #     isHappy = None
# #
# #     def set_data(self, name, age, isHappy):
# #         self.name = name
# #         self.age = age
# #         self.isHappy = isHappy
# #
# #     def get_data(self):
# #         print(self.name, "age", self.age, ". Happy: ", self.isHappy)
# #
# #
# # cat1 = Cat()
# # cat1.set_data("Барсик", 3, True) # Заменили следущие три строчки вводом параметров в метод set.data
# # # cat1.name = "Barsik"
# # # cat1.age = 3
# # # cat1.isHappy = True
# #
# # cat2 = Cat()
# # cat2.name = "Жопен"
# # cat2.age = 2
# # cat2.isHappy = False
# #
# # cat3 = Cat()
# # cat3.set_data("Иван", 5, False)
# #
# # cat1.get_data()
# # cat2.get_data()
# # cat3.get_data()
#
# # print(cat1.name)
# # print(cat2.name)
#
#
# # КОНСТРУКТОРЫ (возможность выполнить сразу какйо-то код при создании объекта)
#
# # class Cat:
# #     name = None
# #     age = None
# #     isHappy = None
# #
# #     def __init__(self, name = None, age = None, isHappy = None): #Конструктор
# #         self.set_data(name, age, isHappy) #получаем данные
# #         self.get_data() #сразу выводим данные
# #
# #     def set_data(self, name = None, age = None, isHappy = None): # None(или любое другое(список, параметр и т.д.) - значение по умолчанию, если параметр не будет задан
# #         self.name = name
# #         self.age = age
# #         self.isHappy = isHappy
# #
# #     def get_data(self):
# #         print(self.name, "age", self.age, ". Happy: ", self.isHappy)
# #
# # cat1 = Cat("Барсик", 3,True) #Установка данных происходит во время создания объекта
# # cat1.set_data("John",2)
# # cat2 = Cat("Жопен", 5, False)
#
# # cat1.get_data()
# # cat2.get_data()
#
#
# # НАСЛЕДОВАНИЕ, ИНКАПСЮЛЛЯЦИЯ, ПОЛИМОРФИЗМ
#
#
# class Building:  # Наследование(наследовать можно только от одного класса)
#     year = None
#     city = None
#         # ...
#
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#
#     def get_info(self):
#         print("Year:", self.year, "City:", self.city)
#
# class School(Building):
#     pupils = 0
#
#     def __init__(self, pupils, year, city):
#         super(School, self).__init__(year, city) #super это основной класс(родитель)
#         self.pupils = pupils
#
#     def get_info(self):#ПОЛИМОРФИЗМ(пишем такой же метод к в Building и вносим доп корректировки)
#         super().get_info()
#         print("Pupils",self.pupils)
#
# class House(Building):
#     pass
#
# class Shop(Building):
#     pass
#
#
# school = School(100, 2000, "Moscow")
# school.get_info()
# house = House(2008, "Piter")
# house.get_info()
# shop = Shop(1999, "Sochi")
# shop.get_info()
#
#
# ##ПОЛИМОРФИЗМ-ИЗМЕНЕНИЕ МЕТОДОВ КЛАССА РОДИТЕЛЯ В КЛАССЕ НАСЛДЕНИКЕ
# ##ИНКАПСУЛЯЦИЯ - ЗАЩИТА ПОЛЕЙ В КЛАССЕ ОТ ИЗМЕНЕНИЙ ВРУЧНУЮ(ДОСТУП К
# ## НИМ ДОЖЕН БЫТЬ ТОЛЬКО ЧЕРЕЗ МЕТОДЫ, ФУНКЦИИ И КОНСТРУКЦИИ)ЗАЩИТА ДАННЫХ,
# # НО В ПИТОНЕ НЕ ОЧЕНЬ РЕАЛИЗОВАНА



# ДЕКОРАТОРЫ ФУНКЦИЙ В PYTHON(с помощью декортора мы можем выполнять какой-либо код ДО и ПОСЛЕ
#определенной функции). По сути это изменение поведения фунции без изменения ее кода




# import webbrowser
#
# def validator(func):
#     def wrapper(url):
#         print("Это текст до функции")
#         func(url)
#         print("Это текст после функции")
#     return wrapper
#
#
# @validator
# def open_url(url):
#     webbrowser.open(url)
#
# open_url("https://itproger.com")



# import webbrowser
#
# def validator(func):
#     def wrapper(url):
#         if "." in url:    #к функции добавлен функционал до ее выполнения с проверкой
#             func(url)
#         else:
#             print(" Неверный URL")
#     return wrapper
#
#
# @validator   # можно добавлять декортаор в несколько функций и каждый раз не прописывать нужный функционал
# def open_url(url):
#     webbrowser.open(url)
#
# open_url("https://itproger.com")


