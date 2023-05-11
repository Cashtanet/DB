# #2.1.1
# a, b = int(input()), int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print((a**10 + b**10)**0.5)



## 2.1.2
# weight = float(input("Введите ваш вес: "))
# height = float(input("Введите ваш рост: "))
#
# imt = weight/height**2
# if 18.5 <= imt <= 25:
#     print("Оптимальная масса")
# elif imt < 18.5:
#     print("Недостаточная масса")
# else:
#     print("Избыточная масса")



## 2.1.3
# s = input()
# length = len(s)
# summ = length * 60
# print(f"{summ // 100} р. {summ % 100} коп.")

## 2.1.4
# s = input().split()
# print(len(s))


## 2.1.5
# year = int(input())
# s = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# print(s[(year + 4)%12])


## 2.1.6
# n = str(int(input()))
# if len(n) == 6:
#     s = n[0] + n[-1:-6:-1]
# else:
#     s = n[::-1]
# print(int(s))

# s = input()
# print(int(s[:-5] + s[-5:][::-1]))


## 2.1.7

# n = int(input())
# print(f"{n:,}")


## 2.1.8
# n = int(input())
# k = int(input())
# s = 0
# for i in range(1, n + 1):
#     s = (s + k) % i
# print(s + 1)

# n = int(input()) #Прикольное решение!!!
# k = int(input())
# list = [i for i in range(1, n + 1)]
#
# while len(list) != 1:
#     for i in range(0, k-1):
#         list.append(list[i])
#     del list[0:k]
#
# print(*list)


# ## 2.2.1
# n = int(input())
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# for i in range(n):
#     q = input().split()
#     if int(q[0]) != 0 and int(q[1]) != 0:
#         if int(q[0]) > 0:
#             if int(q[1]) > 0:
#                 count1 += 1
#             else:
#                 count4 += 1
#         else:
#             if int(q[1]) > 0:
#                 count2 += 1
#             else:
#                 count3 += 1
# print("Первая четверть:", count1)
# print("Вторая четверть:", count2)
# print("Третья четверть:", count3)
# print("Четвертая четверть:", count4)



## 2.2.2
# s = input().split()
# count = 0
# for i in range(len(s) - 1):
#     if int(s[i + 1]) > int(s[i]):
#         count += 1
# print(count)


## 2.2.3
# s = input().split()
#
# for i in range(0, len(s) - 1, 2):
#     s[i + 1], s[i] = s[i], s[i + 1]
#
# print(*s)


## 2.2.4
# s = input().split()
# s.insert(0, s[-1])
# del s[-1]
#
# print(*s)


## 2.2.5
# s = input().split()
# n = len(set(s))
# print(n)

# print(len(set(input().split()))) # вариант в одну строку


## 2.2.6
# n = int(input())
# s = []
# for i in range(n):
#     num = int(input())
#     s.append(num)
# s.remove(0)
# nums = int(input())
# flag = "НЕТ"
# if nums == 0:
#     flag = "ДА"
# if len(s) > 0:
#     for k in range(len(s)):
#         if nums / s[k] in s[k + 1:]:
#                 flag = "ДА"
# print(flag)


## 2.2.7
# timur = input().lower()
# ruslan = input().lower()
# s = ["камень", "ножницы", "бумага"]
#
# if timur == ruslan:
#     print("ничья")
# elif timur == s[0]:
#     if ruslan == s[1]:
#         print("Тимур")
#     else:
#         print("Руслан")
# elif timur == s[1]:
#     if ruslan == s[2]:
#         print("Тимур")
#     else:
#         print("Руслан")
# elif timur == s[2]:
#     if ruslan == s[0]:
#         print("Тимур")
#     else:
#         print("Руслан")



## 2.2.8
# s = ["камень", "ножницы", "бумага", "ящерица", "спок"]
# timur = input().lower()
# ruslan = input().lower()
# if ruslan == timur:
#     print("ничья")
# elif timur == s[0]:
#     if ruslan == s[2] or ruslan == s[4]:
#         print("Руслан")
#     else:
#         print("Тимур")
# elif timur == s[1]:
#     if ruslan == s[0] or ruslan == s[4]:
#         print("Руслан")
#     else:
#         print("Тимур")
# elif timur == s[2]:
#     if ruslan == s[1] or ruslan == s[3]:
#         print("Руслан")
#     else:
#         print("Тимур")
# elif timur == s[3]:
#     if ruslan == s[0] or ruslan == s[1]:
#         print("Руслан")
#     else:
#         print("Тимур")
# elif timur == s[4]:
#     if ruslan == s[2] or ruslan == s[3]:
#         print("Руслан")
#     else:
#         print("Тимур")


## 2.2.9    # ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР (входные данные)
# s = max(input().split("О"))
#
# print(len(s))


## 2.2.10
# n = int(input())
# anton = ["a", "n", "t", "o", "n"]
# ls = []
# for k in range(n):
#     flag = True
#     s = input()
#     for i in anton:
#         if i not in s:
#             flag = False
#             break
#         else:
#             a = s.find(i)
#             s = s[a:]
#
#     if flag == True:
#         ls.append(k + 1)
# print(*ls)


## 2.2.11
# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
# s = input() + " запретил букву"
# for i in alphabet:
#     if i in s:
#         print(s, i)
        # s = s.replace(i, '').replace('  ', ' ')



# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# a = set(alphabet)
# b = list(a)
# b.sort()
# print(b)


##3.1 Типы данных BOOL
# numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
# res = 0
#
# for num in numbers:
#     res += (num % 2 == 0)
# print(res)



# n = 1
# s = '1'
# a = []
# print(bool(a), bool(s), bool(n))
# print(bool(0.0))


##  Функции возвращающие булево значение(такие функции нахываются ПРЕДИКАТОМ)
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(156))



##  Проверяет соответствие типа данных
# print(isinstance(3, float))
# print(isinstance(3.5, float))
# print(isinstance('Beegeek', str))
# print(isinstance([1, 2, 3], list))
# print(isinstance(True, bool))


# print(type(3))
# print(type(3.5))
# print(type('Beegeek'))
# print(type([1, 2, 3]))
# print(type(True))


##3.1.1
# # объявление функции
# def func(num1, num2):
#     return num1 % num2 == 0
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')


#3.2 None and NoneType
#
# var = None
# if var is None:   # используем оператор is
#   print('None')
# else:
#   print('Not None')


##4.2 Вложенные списки
# total = 0
# my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30, 40, 50]]
#
# for li in my_list:
#     total += len(li)
#
# print(total)



##4.2.3
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
#
# print(maximum)


##4.2.4
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
#
# print(list1)


## 4.2.5
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
# print(total/counter)


## 4.3

## 1
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = []
#
# for _ in range(n):
#     my_list.append([0] * m) #создает в каждом элементе списка ссылку на один и тот же список
#
# print(my_list)
#
# ## 2
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
#
# for i in range(n):
#     my_list[i] = [0] * m
#
# print(my_list)


## 3  Верный, в нем каждый новый список это отдельный элемент
# n, m = int(input()), int(input())    # считываем значения n и m
#
# my_list = [[0] * m for _ in range(n)]    #  генератор списка
#
# print(my_list)


## 4.3.1
# n = int(input())
# lst = [i for i in range(1, n + 1)]
# for i in range(n):
#     print(lst)


## 4.3.2
# n = int(input())
# for i in range(n):
#     lst = [i for i in range(1, i + 2)]
#     print(lst)



# ## 4.3.3  #треугольник паскаля вывод строки n
# n = int(input())
#
# def pascal(num):
#     a = [[]for i in range(num)]
#     for i in range(num):
#         for j in range(i+1):
#             if (j < i):
#                 if j == 0:
#                     a[i].append(1)
#                 else:
#                     a[i].append(a[i - 1][j] + a[i - 1][j - 1])
#             elif j == i:
#                 a[i].append(1)
#     return a
#
# print(pascal(n + 1)[-1])



## 4.3.4    #треугольник паскаля
# n = int(input())
#
# def pascal(num):
#     a = [[]for i in range(num)]
#     for i in range(num):
#         for j in range(i+1):
#             if (j < i):
#                 if j == 0:
#                     a[i].append(1)
#                 else:
#                     a[i].append(a[i - 1][j] + a[i - 1][j - 1])
#             elif j == i:
#                 a[i].append(1)
#     return a
#
# b = pascal(n)
# for i in range(n):
#     print(*b[i])


## 4.3.5
# s = input().split()
# char_list = [[s[0]]]
# for i in range(1, len(s)):
#     if s[i] in char_list[-1]:
#         char_list[-1].append(s[i])
#     else:
#         char_list.append([s[i]])
# print(char_list)


# 4.3.6   #делает из строки вложенные списки длины n
# def chunked(lst, num):
#     chunk_list = []
#     for i in range(0, len(lst), num):
#         chunk_list.append(lst[i:i + n])
#
#     return chunk_list
#
# s = input().split()
# n = int(input())
#
# print(chunked(s, n))


# # 4.3.7  # Это пипец))Списал решшение (выводит все подсписки списка из введенных элементов через проьел
# lst_input = input().split()
# plst = []
# lst_output = [[]]
# for i in range(len(lst_input)):
#     for j in range(len(lst_input)):
#         plst = lst_input[j:i + j + 1]
#         if len(plst) == i + 1:
#             lst_output.append(plst)
#
# print(lst_output)


## 4.4 
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# #
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()


# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
#
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(6), end='')  #выравнивание методом ljust
#     print()


# n = 8
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
#
# for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
#
# for r in range(n):                     # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()



# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()


# n = int(input()) #считывание матрицы из n строк заполненной числами
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# print(matrix)


# ## 4.4.1
# n = int(input())
# m = int(input())
# s = []
# for i in range(n):
#     s.append([])
#     for j in range(m):
#         s[i].append(input())
#
# for r in range(n):
#     for c in range(m):
#         print(s[r][c], end=' ')
#     print()


## 4.4.2
# n = int(input())
# m = int(input())
# s = []
# for i in range(n):
#     s.append([])
#     for j in range(m):
#         s[i].append(input())
#
# for r in range(n):
#     for c in range(m):
#         print(s[r][c], end=' ')
#     print()
# print()
# for c in range(m):
#     for r in range(n):
#         print(s[r][c], end=' ')
#     print()


## 4.4.3
# n = int(input())
# s = []
# a = 0
# sum = []
# for i in range(n):
#     s.append(input().split())
#
# sum = [s[k][k] for k in range(n)]
# for j in sum:
#     a += int(j)
# print(a)


##4.4.4

# n = int(input())
# s = []
# a = 0
# sum = []
# for i in range(n):
#     s.append(input().split())
#
# for j in range(n):
#     counter = 0
#     sum1 = 0
#     for k in range(n):
#         sum1 += int(s[j][k])
#     for l in range(n):
#         if float(s[j][l]) > float(sum1/n):
#             counter += 1
#     print(counter)


##4.4.5
#
# n = int(input())
# matrix = []
# maximum = - 2 ** 10
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i >= j and matrix[i][j] > maximum:
#             maximum = matrix[i][j]
# print(maximum)


##4.4.5
# n = int(input())
# matrix = []
# maximum = - 2 ** 500
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= (n - j - 1) or
#            i <= j and i >= (n - j - 1)) and matrix[i][j] > maximum:
#             maximum = matrix[i][j]
# print(maximum)


##4.4.6
# n = int(input())
# matrix = []
# s1, s2, s3, s4 = 0, 0, 0, 0
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for j in range(n):
#     for i in range(n):
#         if i < j:
#             if i < (n - j - 1):
#                 s1 += matrix[i][j]
#             elif i > (n - j - 1):
#                 s2 += matrix[i][j]
#         elif i > j:
#             if i > (n - j - 1):
#                 s3 += matrix[i][j]
#             elif i < (n - j - 1):
#                 s4 += matrix[i][j]
#
# print("Верхняя четверть:", s1)
# print("Правая четверть:", s2)
# print("Нижняя четверть:", s3)
# print("Левая четверть:", s4)


## 4.5.1
# n = int(input())
# m = int(input())
# s = []
# for i in range(n):
#     s.append([])
#     for j in range(m):
#         s[i].append(i * j)
#
# for r in range(n):
#     for c in range(m):
#         print(s[r][c], end=' ')
#     print()


## 4.5.2
# n = int(input())
# m = int(input())
# s = []
# for i in range(n):
#     s.append(input().split())
# maximum = s[0][0]
# x = 0
# y = 0
# for j in range(n):
#     for k in range(m):
#         if int(s[j][k]) > int(maximum):
#             maximum = s[j][k]
#             x = j
#             y = k
# print(x, y)


## 4.5.3
# n = int(input())
# m = int(input())
# s = []
# for i in range(n):
#     s.append(input().split())
# row = input().split()
#
# for k in range(n):
#     s[k][int(row[0])], s[k][int(row[1])] = s[k][int(row[1])], s[k][int(row[0])]
#
# for r in range(n):  #!!!!!запомни уже
#     print(*s[r])


## 4.5.4
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# counter = 0
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if matrix[i][j] == matrix[j][i]:
#                 counter += 1
# if counter == n ** 2 - n:
#     print("YES")
# else:
#     print("NO")


## 4.5.4




































