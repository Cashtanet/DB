# МФТИ Алгоритмы и структуры данных в Python Тимой Федорович

# print("Hello, world!") #не хранит "HW" в памяти
#

# x = "Hello, world!" #именованная (имя x) ссылка на обьект "HW" в памяти
# print(x)
# print(type(x))
# x = 1+2+3+2# новый объект int и потом связывается имя x с ним, а старый объект удаляется
# print(x)

#Сборщик мусора полсе выполнения программы удаляет все неименованные объекты

# a = 2
# b = 3
# a,b = b,a
# print(a)

# x = y = z = 0 #каскадное присваивание
# x,y,z = 1,2,3 #множественное присваивание
#кортеж переменных и кортеж значений

# print(int(25**0.5))#квадратный корень

# a=10
# b=10
# c=5
# print(a/b*c)#операции выполняются последовательно

# Теория групп изучить

# -11//10 = -2 #берется меньшее значение, которое делится на 10(-20)
# -11%10 = 9 #остаток от деления мешьшего числа(-20) на (-12) итого 8

# i = 0
# while i < 10: #заголок цикла
#     i += 1 #тело цикла (итерация - однократное выполнение тела цикла)
#     print(i)
# else: # выполняется на выходе из цикла после всех итераций
#     print('The END')

# for i in range(10):
#     i += 1
#     print(i)

# for x in range(10, 20, 1): #range(start,stop,step) stop верхняя граница, не включается
#         if x > 15:
#             print(x ** 2)
#         else:
#             print(x ** 3)




# ТИП BOOL

# flag = False
#
# n = int(input())
#
# for i in range(n):
#     x = int(input())
#     flag = (x%10 == 0) or flag
#     print(flag)


# flag = True
# n = int(input())
# for i in range(n):
#     x = int(input())
#     flag = (flag and
#             x%10 == 0)
#     print(flag)



# Вложенные и последовательные IF-ы

# x = int(input())
#
# if x%2 == 0:
#     print("1")
# if x%3 == 0:
#     print("2")

# if x == 1 or x == 2:
#     print("yes")
# else:
#     print("no")


# if x%2 == 0:
#     if x%3 == 0:
#         print("na 6")

# if x%2 == 0 and x%3 == 0:
#     print("na 6")
# else:
#     print("ne %6")


# Каскадные условные конструкции

# x = int(input("Введите ваше число: "))
#
# if x < 0:
#     print("a")
# elif x < 5:
#     print("b")
# elif x < 10:
#     print('c')
# else:
#     print('d')




# x = int(input("Введите x: "))   #определение координатной плоскости
# y = int(input("Введите y: "))
#
# if y > 0:
#     if x > 0:
#         print("I")
#     else:
#         print("II")
# else:
#     if x > 0:
#         print("IV")
#     else:
#         print("III")



# цифра - символ для кодирования числа

# a = 2**14
# b = 2**13
# c = 2**12
# d = 2**10
# e = 2**9
# f = 2**8
# g = 2**7
# i = 2**5
# j = 2**3
# k = 2
# print(a + b + c + d + e + f + g + i + j + k)



# x = 0b111101  #запись бинарного числа
# y = 0o0732 #запись 8ричной системы
# z = 0x1f #запись 16ричного числа
# t = int('z3f', 36) #36 ричная
#
# print(x)
# print(y)
# print(z)
# print(t)


# x = 127
# print(bin(x)) #печать бинарной версию числа
# print(oct(x)) #печать 8ричной версию числа
# print(hex(x)) #печать 16ричной версию числа

#
# base = 2
# x = int(input())    #перевод числа в 10чную систему из любой
# while x>0:
#     digit = x%base
#     print(digit, end = '')
#     x//=base



#ФУНКЦИИ


# def hello():
#     print("Hello, world!")
#
# hello()   #скобки являются признаком вызова функции
# f = hello
# f()


# name = input("Введите ваше имя: ")
# def hello(name): #функция с параметром(можно несколькими)
#     print("Hello,", name, "!")
# hello(name)


# name = input("Введите ваше имя: ")
# def hello(name = "world"): #world значение по умолчанию
#     print("Hello,", name, "!")
# hello()


# def max2(x, y): #функция максимального из двух
#     if x > y:
#         return x #return прекращает выполение функции
#     return y #else не нужен получается
#
#
# def max3(x, y, z):
#     return max2(x, max2(y, z))
#
# print(max3(36,12.6,7.2))
# print(max3("ab", "abc", "abd"))  #Duck typing, утиный полиморфизм/типизация
# ## любое нечто, которое можно сравнивать друг с другом допустимо в качетсве
# ## аргументов этой функции



# def hello_separated(name = "World", separator = "-"):
#     print("Hello", name, sep=separator)
#
# hello_separated("John","***")
# hello_separated(separator="***")
# hello_separated(name="John")    #именованные параметры



## СИНХРОННОЕ ВЫПОЛНЕНИЕ (по умолчанию)
## В момент вызова функции, основная программа останавливается и подолжит работу
## после выполнения функции


## СТЭК вызовов, CALL STACK. (область памяти, хранящая адреса возвратов
## от функций, куда функции вернуть значение после ее выполнения)



## СТРУКТУРНОЕ ПРОГРАММИРОВАНИЕ (приложение не будет большим, без
## понимания архитектуры и его структуры. Функции нужны для
## повторяющихся участков кода

#Проектирование "сверху вниз":#



# import graphics as gr
#
# def build_house(window, upper_left_corner, width): #функция пустышка (pass - ничего не делать, формально создает тело функции)
#     """функция которая рисует дом""" #документ строка
#     height = calculate_height(width)
#
#
# window = gr.GraphWin("Russian game", 300, 300)
# build_house(window, gr.Point(100,100), 100)
# print("Ура! Дом построен!")



# МЕТОД ГРУБОЙ СИЛЫ (BRUTE FORCE) перебор подярд значений

# есть область определение и множество значений



# def is_simple_number(x):
#     """ Определяет, является ли число простым
#         x - целое положительное число
#         Если простое, то возвращает True, иначе False
#     """
#     divisor = 2
#     while divisor < x:
#         if x%divisor == 0:
#             return False
#         divisor += 1
#     return True
#
# print(is_simple_number(18))



# def factorize_number(x):
#     """ Раскладывает число на множители
#     печатает их на экран
#     """
#     divisor = 2
#     while x > 1:
#         if x%divisor == 0:
#             print(divisor)
#             x//= divisor
#         else:
#             divisor += 1
#
# print(factorize_number(999))


# a = [1, 2, 3, 4, 5]
# for x in a:
#     print(x)
#     x += 1
#     print(x)
# # print(a)

# b = a[2]
# print(b)

#
# a = [0]*10
# print(a)

# import this

# a = int(input())
# if a%4 == 0:
#     print(a//4)
# else:
#     print(a//4 +1)

# a = int(input())
# print(a, "мин - это", a//60, "час", a%60, "минут")

# a = int(input())
# print("Сумма цифр =", a//100 + a%100//10 + a%10)
# print("Произведение цифр =", (a//100) * (a%100//10) * (a%10))

#
# a, b, c = map(int, input())
# print("Сумма цифр =", a + b + c)
# print("Произведение цифр =", c * b * a)

# d = int(input())
# a = d//100
# b = d%100//10
# c = d%10
# print(a,b,c, sep='')
# print(a,c,b, sep='')
# print(b,a,c, sep='')
# print(b,c,a, sep='')
# print(c,a,b, sep='')
# print(c,b,a, sep='')

# n = list(input())
#
# for x in range( len(n)):
# 	for y in range( len(n)):
# 		for z in range( len(n)):
# 			if x != y and x != z and z != y:
# 				print(n[x] + n[y] + n[z])


# print(17*"*")
# print("*", 15*" ", "*", sep='')
# print("*", 15*" ", "*", sep='')
# print(17*"*")

# a = int(input())
# b = int(input())
# print("Квадрат суммы", a, "и", b, "равен", (a + b)**2)
# print("Сумма квадратов", a, "и", b, "равна", a**2 + b**2)


# n = int(input())
# print((n + 10*n+100*n)+(n + 10*n) + n)
# print(n * 123)

# a = int(input())
# if a//1000 + a%10 == a%1000//100 - a%100//10:
#     print("ДА")
# else:
#     print("НЕТ")


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b:
#     a = b
# if c > d:
#     c = d
# if a > c:
#     a = c
# print(a)


# a = int(input())
# v1, v2, v3, v4 = a <= 13, 14 <= a <= 24, 25 <= a <= 59, 60 <= a
# print(v1 * 'детство' + v2 * 'молодость' + v3 * 'зрелость' + v4 * 'старость')
# print(v1)

# a, b, c = int(input()), int(input()), int(input())
# d, e, f = 0, 0, 0
# if a > 0:
#     d = a
# if b > 0:
#     e = b
# if c > 0:
#     f = c
# print(d + e + f)


# x = int(input())
# if x <= -3 or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# a, b, c = int(input()), int(input()), int(input())
# if (a >= b + c) or (b >= a + c) or (c >= a + b):
#     print("NO")
# else:
#     print("YES")



# y = int(input())
# if y%4 == 0 and not y%100 == 0 or y%400 == 0:
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a - c == 1) or (a - c == -1) or (a - c == 0) and (b - d == 1) or (b - d == -1) or (b - d == 0):
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x1-x2 == 1 or x1-x2  == -1 or x1-x2  == 0) and (y1-y2 == 1 or y1-y2 == -1 or y1-y2 == 0):
#     print('YES')
# else:
#     print('NO')


# a = int(input())
# b = int(input())
# s = str(input())
# if s == "*":
#     print(a * b)
# elif s == "/" and b != 0:
#     print(a/b)
# elif s == "/" and b == 0:
#     print("На ноль делить нельзя!")
# elif s == "+":
#     print(a + b)
# elif s == "-":
#     print(a - b)

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if a1%2 == b1%2 and a2%2 == b2%2 or a1%2 != b1%2 and a2%2 != b2%2:
#     print("YES")
# else:
#     print("NO")


#
# a = float(input())
# if a == 0:
#     print("Обратного числа не существует")
# else:
#     print(1/a)


# a = input()  #ищет минимум и максимум по ключу
# b = input()
# c = input()
# print(min(a, b, c, key=len))
# print(max(a, b, c, key=len))

# s = input()
# if "суббота" or "воскресенье" in s:
#     print("YES")
# else:
#     print("NO")


# from math import *
# print(sqrt(25))
# print(ceil(2.25))
# print(floor(12.5))
# print(log10(1000000))
# print(log2(4096))


# from math import *
# x = float(input())
# r = x * pi / 180
# print(sin(r) + cos(r) + tan(r)**2)

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')


# n = int(input())
# if n >= 2:
#     for i in range(n+1):
#         print((n- i) * "*")


# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     r = m * (1 + p / 100)**i
#     print((i+1), r)


# for i in range(100, 200):  # перебираем числа от 100 до 999
#     if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)


# largest = int(input())  # принимаем первое число за максимальное
# for i in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest

# total = 0
# for i in range(1, 6):
#     total += i
    # print(total, end='')

# a = int(input())
# b = int(input())
# counter = 0
# i = 1
# for i in range(a, b+1):
#     if i**3%10 == 4 or i**3%10 == 9:
#         counter += 1
# print(counter)


# n = int(input())
# sum = 0
# for i in range(n):
#     a = int(input())
#     sum += a
# print(n, sum, sep="\n")


# n = int(input())
# bigger = 0
# second = 0
# for i in range(1, n+1):
#     a = int(input())
#     if a > bigger:
#         second = bigger
#         bigger = a
# print(second)
# print(bigger


# a = 1           #Фебоначчии!!!!!!!!!!!!!!!!!!!!
# b = 0
# n = int(input())
# for i in range(n):
#     f = a + b
#     b = f
#     a = f - a
#     print(f, end=" ")
#     f = a + b


# x = y = 1
# for _ in range(int(input())):
#     print(x, end=' ')
#     x, y = y, x + y


# i = int(input())
# while i != 1:
#     print(i**2)
#     i = int(input())
# print("Ты ввел 1 ублюдок!")


# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print



# p = int(input()) #минимальное число монет для суммы (номинал 25.10.5.1)
# counter = 0
# while p >= 25:
#     counter += 1
#     p = p -25
# while p >= 10:
#     counter += 1
#     p = p -10
# while p >= 5:
#     counter += 1
#     p -= 5
# while p > 0:
#     counter += 1
#     p -= 1
# print(counter)



# n = int(input())
# counter = 0
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10
#     # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10
#     counter += last_digit
# print(counter)


# num = int(input())
# has_seven = False  # сигнальная метка

# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# while n != 0:
#     ld = n%10
#     print(ld)
#     n = n//10

# n = int(input())
# mx = 0
# mn = 9
# while n != 0:
#     ld = n%10
#     if ld > mx:
#         mx = ld
#     if ld < mn:
#         mn = ld
#     n = n//10
# print("Максимальная цифра равна", mx)
# print("Минимальная цифра равна", mn)


# summa = 0
# colvo = 0
# umnoj = 1
# sred = 0
# first = 0
# sumfisrtlast = 0
# n = int(input())
# s = str(n)
# last = n%10
# while n != 0:
#     ld = n % 10
#     summa += ld
#     colvo += 1
#     umnoj *= ld
#     n = n // 10
#
# print(summa)
# print(colvo)
# print(umnoj)
# print(summa/colvo)
# print(s[0])
# print(int(s[0])+last)


# n = int(input())
# s = str(n)
# print(s[1])


# n = int(input())
# x = True
# while n != 0:
#     ld = n%10
#     n = n//10
#     d = n%10
#     if ld != d:
#         x = False
# if x == False:
#     print("NO")
# else:
#     print("YES")


# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)


# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
#
# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Цикл завершен.')


# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# num = int(input())
# flag = True
#
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
#         break
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)



# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)



# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for k in range(1, 10):
#         print(i, "+", k, "=", i + k)
#     print()


# n = int(input())
# for i in range(n//2+2):
#     print(i * "*")
# for i in range(n//2, 0, -1):
#     print(i * "*")
#


# for n in range(1,14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(n, k, m)


# for n in range(1,100):
#     for k in range(1, 100):
#         for m in range(1, 100):
#             if 10 * n + 5 * k + 0.5 * m == 100 and m + n + k == 100:
#                 print(n, k, m)


# for a in range(1, 150):
#     for b in range(1, 150):
#         for c in range(1, 150):
#             for d in range(1, 150):
#                 for e in range(1, 150):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a + b + c + d + e)


# n = int(input())
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=' ')
#         num += 1
#     print()


# n = int(input())
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=' ')
#         num += 1
#     print()


# n = int(input())
# for k in range(1, n + 1):
#     for i in range(1, k + 1):
#         print(i, end='')
#     for i in range(k - 1, 0, -1):
#         print(i, end='')
#     print()


# a = int(input()) # программа из дапазона чисел выводит число с максимальной суммой его делителей и сумму этих делителей

# b = int(input())
# dig = 0
# delit = 0
# for i in range(a, b + 1):
#     count = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             count += k
#             if count >= delit:
#                 delit = count
#                 dig = i
# print(dig, delit)


# n = int(input())
# num = 0
# for i in range(1, n + 1):
#     count = 0
#     plus = str()
#     for k in range(1, i + 1):
#         if i%k == 0:
#             plus += "+"
#             num = i
#     print(num, plus, sep='')


# n = int(input())
# while n > 9:
#     count = 0
#     while n > 0:
#         last = n%10
#         count += last
#         n = n//10
#     n = count
# print(n)


# print((int(input()) - 1) % 9 + 1)

# n = int(input())
# summa = 0
# for i in range(1, n + 1):
#     factroial = 1
#     for k in range(1, i + 1):
#         factroial *= k
#     summa += factroial
# print(summa)



# a = int(input())  #ищет в заданном диапазоне простые числа и выводит  их на экран
# b = int(input())
# for x in range(a, b + 1):
#     counter = 0
#     for i in range(1, x + 1):
#         if x%i == 0:
#             counter += 1
#     if counter == 2:
#         print(x)

# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)

# n = int(input())
# s = 0
# while n > 9:
#     if n % 2 == 0:
#         s = n % 10
#     n //= 10
# print(s)


# n = int(input())
# count3 = 0
# count_last = 0
# count_even = 0
# summa_5 = 0
# umn7 = 1
# count_0_5 = 0
# last = n%10
# while n > 0:
#     if n % 10 == 3:
#         count3 += 1
#     if last == n%10:
#         count_last += 1
#     if (n%10)%2 == 0:
#         count_even += 1
#     if n%10 > 5:
#         summa_5 += n%10
#     if n%10 > 7:
#         umn7 *= n%10
#     if n%10 == 0 or n%10 == 5:
#         count_0_5 += 1
#     n = n // 10
# print(count3)
# print(count_last)
# print(count_even)
# print(summa_5)
# print(umn7)
# print(count_0_5)

# s = input()
# flag = "Цифр нет"
# for i in range(len(s)):
#     if s[i] in ("0123456789"):
#         flag = "Цифра"
# print(flag)

# s = input()      #считает количество гласных и согласных в строке
# glas = 0
# soglas = 0
# for i in range(len(s)):
#     if s[i] in ("ауоыиэяюёе"):
#         glas += 1
#     elif s[i] in ("бвгджзйклмнпрстфхцчшщ"):
#         soglas += 1
# print("Количество гласных букв равно", glas)
# print("Количество согласных букв равно", soglas)

# n = int(input())

# s = input()  #разворот строки
# print(s[::-1])

#
# n = int(input())  #перевод десятичного в двоичную
# s = ""
# while n != 0:
#     s = str(n%2) + s
#     n //= 2
# print(s)


# s = input()  #Тест на слово ПОЛИНДРОМ
# if s == s[::-1]:
#     print("YES")
# else:
#     print("NO")


# s = input()  #Разделяет стоку на две и соединяет конец с началом в обратном порядке
# a = ""
# b = ""
# if len(s)%2 == 0:
#     a = s[:int(len(s)/2)]
#     b = s[int(len(s)/2):]
#     print(b + a)
# else:
#     a = s[:int(len(s)//2 + 1)]
#     b = s[(len(s)//2 + 1):]
#     print(b + a)



# s = input()
# if s.endswith(".ru") or s.endswith(".com"):
#     print("YES")
# else:
#     print("NO")

#
# s = input()  #находит наиболее повторяющийся символ
# count_max = 0
# char = 0
# for i in s:
#     if s.count(i) >= count_max:
#         count_max = s.count(i)
#         char = i
# print(char)


# s = input()
# if s.count("f") == 1:
#     print(s.index("f"))
# elif s.count("f") > 1:
#     print(s.index("f"), s.rindex("f"))
# else:
#     print("NO")

#
# a = int(input())  #выводит символы по коду из UNICODE в диапазон a b
# b = int(input())
# for i in range(a, b + 1):
#     print(chr(i), end = ' ')


# s = input()
# for i in range(len(s)):
#     print(ord(s[i]), end=' ')


# n = int(input())  #шифр цезаря(декоидровка сообщения по ключу)
# s = input()
# for i in range(len(s)):
#     a = ord(s[i])
#     if (a - n) < 97:
#         a = a + 26
#     print(chr(a - n), end='')


# s = input()
# count = s.count("f")
# counter = 0
# if count == 0:
#     print(-2)
# elif count == 1:
#     print(-1)
# elif count > 1:
#     for i in range(len(s)):
#         if s[i] == "f":
#             counter += 1
#             if counter ==2:
#                 print(i)


# s = input()
# a = s.find("h")
# b = s.rfind("h")
# c = s[a + 1: b]
# c = c[::-1]
# s = s[: a + 1] + c + s[b:]
# print(s)


# n = int(input())
# s = ''
# for i in range(97, 97 + n):
#     s += chr(i)
# print(list(s))


#
# list = []
# for i in range(1, 27):
#     s = chr(96 + i) * i
#     list.append(s)
# print(list)


# n = int(input())  #Созадет список делителей введенного числа
# lis = []
# for i in range(1, n + 1):
#     if n%i == 0:
#         lis.append(i)
# print(lis)

# lis = []
# lis2 = []
# n = int(input())
# for i in range(n):
#     num = int(input())
#     lis.append(num)
# for k in range(len(lis) - 1):
#     a = lis[k] + lis[k + 1]
#     lis2.append(a)
# print(lis2)



# n = int(input())
# lis = []
# str = ''
# str2 = ''
# for i in range(n):
#     s = input()
#     lis.append(s)
# k = int(input())
# for j in range(len(lis)):
#     str = lis[j]
#     if len(str) >= k:
#         print(str[k - 1], end='')


# n = int(input())
# lst = []
# for i in range(n):
#     s = input()
#     lst += list(s)
# print(lst)


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#
# print(*numbers, sep="\n")

# s = 'Python'
#
# print(*s)
# print()
# print(*s, sep='\n')
#

# n = int(input())
# f = 0
# x_lst = []
# for i in range(n):
#     x = int(input())
#     x_lst.append(x)
# print(*x_lst, sep='\n')
# print()
# for k in x_lst:
#     f = int(k) ** 2 + 2 * int(k) + 1
#     print(f)

# lst = []  #Удаление минимального и максимального значения из списка
# n = int(input())
# for i in range(n):
#     x = int(input())
#     lst.append(x)
# lst.remove(min(lst))
# lst.remove(max(lst))
# print(*lst, sep='\n')


# lst = [] #удаляет дюбли строк и выводит список без дубликатов
# n = int(input())
# for i in range(n):
#     x = input()
#     if x not in lst:
#         lst.append(x)
# print(*lst, sep="\n")



# lst = []  #поиск запроса в введенных строках и вывод этих строк
# n = int(input())
# for i in range(n):
#     x = input()
#     lst.append(x)
# request = input()
# for k in range(n):
#     if request.lower() in lst[k].lower():
#         print(lst[k])


# request = []
# string = []
# result = []
# counter = 0
# n = int(input())
#
# for i in range(n):
#     str1 = input()
#     string.append(str1)
#
# k = int(input())
#
# for l in range(k):
#     req = input()
#     request.append(req)
#
# for j in range(n):
#     for p in range(k):
#         if request[p].lower() in string[j].lower():
#             counter += 1
#             if counter == k:
#                 result.append(string[j])
#                 counter = 0
#
# print(*result, sep="\n")


# n = int(input())  #выводит сроки где есть все введенные запросы
# s = []
# s1 = []
# for i in range(n):
#     x = input()
#     s.append(x)
# k = int(input())
# c = []
# for j in range(k):
#     x = input()
#     c.append(x)
# for l in range(n):
#     counter = 0
#     for m in range(k):
#         counter += 0
#         if c[m].lower() in (s[l].lower()):
#             counter +=1
#     if counter == k:
#         print(s[l])

#
# address = input()
# l = address.split('\\')
# print(*l, sep="\n")


# s = input()
# lis = s.split()
# for i in range(len(lis)):
#     print(int(lis[i]) * "+")


# ip = input()
# counter = 0
# ip_list = ip.split(".")
# for i in range(len(ip_list)):
#     if 0 <= ip_list[i] <= 255:
#         counter += 1
#     if counter == 4:
#         print("ДА")
#     else:
#         print("НЕТ")


# string = input()
# counter = 0
# lis = string.split()
# for i in range(len(lis)):
#     for j in range(i + 1):
#         if lis[i] == lis[j]:
#             counter += 1
# print(counter)

# n = input()  #поменять местами мин и макс элементы списка
# s = n.split()
# s = [int(i) for i in s]  #привозит элементы списка к INT
# a = s.index(min(s))
# b = s.index(max(s))
# s[a], s[b] = s[b], s[a]
# print(*s)



# text = input()
# counter = 0
# s = text.split()
# for i in range(len(s)):
#     if s[i].lower() == "a" or s[i].lower()  == "an" or s[i].lower()  == "the":
#         counter += 1
# print("Общее количество артиклей:", counter)


# n = input()
# n = n[1:len(n) + 1]
# for i in range(int(n)):
#     s = input()
#     if "#" in s:
#         print(s.rstrip(s[0:s.find("#") + 1]))
#     else:
#         print(s)


# n = input()
# n = n.split()
# n = [int(i) for i in n]
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)


# n = int(input())
# lines = [input() for _ in range(n)]
# print(lines)


# evens = [i for i in range(21) if i % 2 == 0]
# print(evens)


# evens = [i for i in range(0, 21, 2)]
# print(evens)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [n[1: len(n)] for n in keywords]
# print(new_keywords)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [n for n in keywords if len(n) >= 5]
#
# print(lengths)


# palindromes = [n for n in range(100, 1001) if str(n) == str(n)[::-1]]
#
# print(palindromes)


# n = int(input())
# lis = [i**2 for i in range(1, n)]
# print(*lis, sep='\n')


# n = input()
# lis = n.split()
# lis2 = [int(i)**3 for i in lis]
# print(lis2)


# s = input()
# k = [i for i in s if i in ("0123456789")]
# print(''.join(k))

# n = input()
# lis = n.split()
# lis2 = [int(i)**2 for i in lis if int(i)%2 != 1 and (int(i)**2)%10 != 4]
# print(lis2)


# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]  #Пузырьковая сортировка
# n = len(a)
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)



##Сортировка выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# for i in range(0, n - 1):
#         smallest = i
#         for j in range(i + 1, n):
#             if a[j] < a[smallest]:
#                 smallest = j
#         a[i], a[smallest] = a[smallest], a[i]
# print(a)



# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(1, n): ##сортировка вставкой
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
#
#
# print('Отсортированный список:', a)


#
# s = input()
# l = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
# for i in range(len(l)):
#     if l[i].lower() in s.lower():
#         print(True)
#         break
#     else:
#         print(False)
#         break


# n = int(input())
# lst = [i for i in range(n + 1) if i%2 == 0]
# print(lst)


# s1 = input()
# s2 = input()
# l = s1.split()
# m = s2.split()
# n = []
# for i in range(len(l)):
#     n.append(int(l[i]) + int(m[i]))
# print(*n)


# s1 = input().split()
# summ = 0
# for i in range(len(s1)):
#     summ += int(s1[i])
# print(*s1, sep="+", end="=")
# print(summ)

# s = input()
# n = s.split("-")
# if "".join(n).isdigit() == True:
#     if s[0] == "7" and s[1] == s[5] == s[9] == "-" or s[3] == s[7] == "-" :
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")



# s = input().split()  #выводит длину самого длинного слова в строке
# n = max([len(i) for i in s])
# print(n)

# s = input().split()
# n = [(i[1:] + i[0][0] + "ки") for i in s]
# print(*n)


# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
#
# draw_box()
# print()
# draw_box()
# print()
# draw_box()


# # объявление функции
# def draw_box():
#     print("*" * 10)
#     for i in range(12):
#         print("*", 6 * " ", "*")
#     print("*" * 10)
#
# # основная программа
# draw_box()  # вызов функции



# def draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
#
# draw_box(int(input()), int(input()))


# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)
#
# n = 10
# m = 7
# draw_box(n, m)
# # print(n, m)



# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, base//2 + 1):
#         print(i * fill)
#     for i in range(base//2 + 1, 0, -1):
#         print(i * fill)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)




# # объявление функции
# def print_fio(name, surname, patronymic):
#     fio = surname[0] + name[0] + patronymic[0]
#     print(fio.upper())
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# # объявление функции
# def print_digit_sum(num):
#     sum = 0
#     for i in range(len(str(n))):
#         sum += int(str(n)[i])
#     print(sum)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)



# # объявление функции
# def get_days(month):
#     if month == 2:
#         return 28
#     elif month in [4, 6, 9, 11]:
#         return 30
#     else:
#         return 31
#
# # считываем данные
## num = int(input())
#
# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def find_all(target, symbol):
#     lst = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             lst.append(i)
#     return lst
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# def merge(list1, list2):
#     s = list1 + list2
#     s = sorted(s)
#     return s
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# def quick_merge():
#     total_list = []
#     n = int(input())
#     for i in range(n):
#         num = [int(q) for q in input().split()]
#         total_list += sorted(num)
#     total_list.sort()
#     total_list = " ".join(total_list)
#     return total_list
#
# print(quick_merge())







# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
# l1 = []
# l2 = []
# n = int(input())
# for i in range(n):
#     l2 = [int(i) for i in input().split()]
#     l1 = quick_merge(l1, l2)
# print(*l1)


# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#
#     if (side1 >= side2 + side3) or (side2 >= side1 + side3) or (side3 >= side1 + side2):
#         return False
#     else:
#         return True
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))



# # объявление функции
# def is_password_good(password):
#     flag = True
#     if len(password) < 8:
#         flag = False
#     if password == password.upper():
#         flag = False
#     if password == password.lower():
#         flag = False
#     counter = 0
#     for i in range(len(password)):
#         if password[i] in "0123456789":
#             counter += 1
#     if counter == 0:
#         flag = False
#     return flag
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_password_good(txt))



# def is_one_away(word1, word2):
#     counter = 0
#     flag = True
#     if len(word1) != len(word2):
#         flag = False
#     for i in range(len(word1)):
#         if word1[i] == word2[i]:
#             counter += 1
#     if len(word1) - counter != 1:
#         flag = False
#     return flag
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))



# # объявление функции
# def is_palindrome(text):
#     s = ''
#     for i in text:
#         if i.isalpha():
#             s += i
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#     print(s)
#
#
# # считываем данные
# txt = input().lower()
#
# # вызываем функцию
# print(is_palindrome(txt))




# # объявление функции
# def is_valid_password(password):
#     counter = 0
#     flag = True
#     s = password.split(":")
#     if len(s) > 3:
#         flag = False
#     if s[0] != s[0][::-1]:
#         flag = False
#     counter2 = 0
#     for i in range(1, int(s[1]) + 1):
#         if int(s[1])%i == 0:
#             counter2 += 1
#     if counter2 > 2:
#         flag = False
#     if int(s[2])%2 != 0:
#         flag = False
#
#     return flag
#
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))



# # объявление функции
# def is_correct_bracket(text):     ## проверяет правильность скобочной послежовательности
#     flag = True
#     counter = 0
#     if text[0] != "(" or text[-1] != ")":
#         flag = False
#     for i in text:
#         if i == "(":
#             counter += 1
#         if i == ")":
#             counter -= 1
#         if counter < 0:
#             flag = False
#             break
#     if counter != 0:
#         flag = False
#
#     return flag
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_correct_bracket(txt))


# # объявление функции
# def convert_to_python_case(text):
#     lst = []
#     s = text[0].lower()
#     for i in range(1, len(text)):
#         if text[i].isupper() == True:
#             s = s + "_" + text[i].lower()
#         else:
#             s += text[i]
#     return s
#
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))


# from math import *
#
# def solve(a, b, c):
#     D = b ** 2 - 4 * a * c
#     if a != 0:
#         if D > 0:
#             x11 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#             x22 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#             return min(x11, x22), max(x11, x22)
#         elif D == 0:
#             x11 = -b / (2 * a)
#             return x11, x11
# a, b, c = int(input()), int(input()), int(input())
#
# x1, x2 = solve(a, b, c)
# print(x1, x2)



# # объявление функции
# def draw_triangle():
#     a = 15
#     h = 8
#     for i in range(h):
#         print((h - 1) * " " + (a - 14) * "*")
#         h -= 1
#         a += 2
#
# # основная программа
# draw_triangle()  # вызов функции


# # объявление функции
# def get_shipping_cost(quantity):
#     if quantity == 1:
#         return 1000 * quantity
#     elif quantity > 1:
#         return (quantity - 1) * 120 + 1000
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


# def factor(a):
#     s = 1
#     for i in range(1, a+1):
#         s *= i
#     return s
#
#
# def compute_binom(n, k):
#     binom = factor(n) / (factor(k) * factor(n - k))
#     return int(binom)
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))




# # объявление функции
# def number_to_words(num):
#     tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
#             'девяносто']
#     ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
#              'восемнадцать', 'девятнадцать']
#     if 1 <= num <= 9:
#         return ones[num]
#     if num == 10:
#         return tens[1]
#     if 10 < num <20:
#         return teens[num - 10]
#     if num >= 20:
#         return tens[num//10] + " " + ones[num%10]
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(number_to_words(n))




# # объявление функции
# def get_month(language, number):
#     ru = ["", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
#     en = ["", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
#     if language == "ru":
#         return ru[number]
#     if language == "en":
#         return en[number]
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))


# # объявление функции
# def is_magic(date):
#     s = date.split(".")
#     if int(s[0]) * int(s[1]) == int(s[2])%100:
#         return True
#     else:
#         return False
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))


# # объявление функции
# def is_pangram(text):
#     s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     flag = True
#     for i in range(len(s)):
#         if s[i] not in text.lower():
#             flag = False
#     return flag
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))



# import random
#
# num1 = random.randrange(15)
# num2 = random.randint(-5, 5)
#
# print(num1)
# print(num2)


# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')


# import random
# c = random.randint(1, 100)
# print("Добро пожаловать в числовую угадайку")
#
# def is_valid(s):
#     return s.isdigit() and 1 <= int(s) <= 100
#
# from math import *   #за сколько попыток угадает число в диапазон от 1 до n
# n = int(input())
#
# is_valid(n)
# a = int(ceil(log(n, 2)))
#
# print(a)





