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
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     # for k in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for r in range(n):
#     print(*matrix[r])  # !!!!!запомни уже


## 4.5.5
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# for i in range(n - 1, -1, -1):
#     print(*matrix[i])


## 4.5.6
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         print((matrix[n - j - 1][i]), end=" ")
#     print()


##4.5.7 #ход коня на поле после ввода клетки типа f5
# matrix = [['.' for _ in range(8)] for _ in range(8)]
# char = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# num = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
#
# n = [_ for _ in input()]
# matrix[num[n[1]]][char[n[0]]] = "N"
#
# for i in char:
#     for k in num:
#         if (char[i] - char[n[0]])**2 + (num[k]- num[n[1]])**2 == 5:
#             matrix[num[k]][char[i]] = "*"
#
# for k in range(8):
#     print(*matrix[k])


##4.5.8
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# flag = "YES"
# k = 0
# for _ in range(n):
#     k += int(matrix[0][int(_)])
#
# for i in range(n):
#     for j in range(n):


##4.6.1
# s = input()
# n, m = int(s.split()[0]), int(s.split()[1])
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         if (i + j)%2 == 0:
#             matrix[i].append(".")
#         else:
#             matrix[i].append("*")
#
# for r in range(n):
#     print(*matrix[r])


##4.6.2
# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(n):
#         if i == n - j - 1:
#             matrix[i].append("1")
#         elif i < n - j - 1:
#             matrix[i].append("0")
#         else:
#             matrix[i].append("2")
#
# for r in range(n):
#     print(*matrix[r])


##4.6.3
# n, m = [int(i) for i in input().split()]
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(1, m + 1):
#         matrix[i].append(i * m + j)
#
# for r in range(n):
#     for p in range(m):
#         print(str(matrix[r][p]).ljust(3), end=" ")
#     print()


##4.6.4
# n, m = [int(i) for i in input().split()]
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         matrix[i].append(i + j * n + 1)
#
# for r in range(n):
#     for p in range(m):
#         print((str(matrix[r][p])).ljust(3), end=" ")
#     print()


##4.6.5
# n = int(input())
# matrix = [[0]*n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j or i == (n - j - 1):
#             matrix[i][j] = "1"
#
# for r in range(n):
#     print(*matrix[r])


##4.6.6
# n = int(input())
# matrix = [[1]*n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i > n - j - 1 or i > j and i < n - j - 1:
#             matrix[i][j] = "0"
#
# for r in range(n):
#     print(*matrix[r])


##4.6.7 # заполнение со смещением
# n, m = [int(i) for i in input().split()]
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         if j + i <= m - 1:
#             matrix[i].append(j + i + 1)
#         else:
#             matrix[i].append((i + j) % m + 1)
#
# for r in range(n):
#     print(*matrix[r])


##4.6.8
# n, m = [int(i) for i in input().split()]
# matrix = []
# for i in range(n):
#     matrix.append([])
#     for j in range(1, m + 1):
#         if i%2 == 0:
#             matrix[i].append(i * m + j)
#         else:
#             matrix[i].append(i * m + m - j + 1)
#
# for r in range(n):
#     for p in range(m):
#         print(str(matrix[r][p]).ljust(3), end=" ")
#     print()


##4.6.9  # заполнение диагоналями
# n, m = [int(i) for i in input().split()]
# matrix = [["."]*m for _ in range(n)]
#
# num = 0
# for q in range(n * m):
#     for i in range(n):
#         for j in range(m):
#             if i + j == q:
#                 num += 1
#                 matrix[i][j] = num
#
# for r in range(n):
#     for p in range(m):
#         print(str(matrix[r][p]).ljust(3), end=" ")
#     print()


## 4.6.10!!!!!!!!!!!! #Заполнение по спирали
# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# dr, dc, r, c = 0, 1, 0, 0
#
# for cnt in range(1, n * m + 1):
#     a[r][c] = cnt
#
#     if a[(r + dr) % n][(c + dc) % m]:
#         dr, dc = dc, -dr
#
#     r += dr
#     c += dc
#
# for row in a:
#     print(*(f'{e:<3}' for e in row), sep='')



## разобраться!"!!!
# [n, m] = [int(num) for num in input().split()]
# matr = [[0] * m for _ in range(n)]
# w = 1
# for k in range(min(n // 2 + 1, m //2 + 1)):  # количество оборотов
#     for j in range(k, m - k):  # заполнение вправо
#         if matr[k][j] == 0:  # условие избавляет от перезаписывания значений
#             matr[k][j] = w
#             w += 1
#     for i in range(1 + k, n - k):  # заполнение вниз
#         if matr[i][m - k - 1] == 0:
#             matr[i][m - k - 1] = w
#             w += 1
#     for j in range(m - k - 2, k - 1, -1):  # заполнение влево
#         if matr[n - k - 1][j] == 0:
#             matr[n - k - 1][j] = w
#             w += 1
#     for i in range(n - k - 2, k, -1):  # заполнение вверх
#         if matr[i][k] == 0:
#             matr[i][k] = w
#             w += 1
# for i in range(n):  # вывод матрицы
#     for j in range(m):
#         print(str(matr[i][j]).ljust(3), end=' ')
#     print()


## 4.7.1 # сложение матриц
# [n, m] = [int(num) for num in input().split()]
# matrix1 = [input().split() for _ in range(n)]
# input()
# matrix2 = [input().split() for _ in range(n)]
# matrix_res = []
# for i in range(n):
#     matrix_res.append([])
#     for j in range(m):
#         matrix_res[i].append(int(matrix1[i][j]) + int(matrix2[i][j]))
#
# for i in range(n):  # вывод матрицы
#     for j in range(m):
#         print(str(matrix_res[i][j]), end=' ')
#     print()


## 4.7.2 #перемножение матриц
# [n, k1] = [int(num1) for num1 in input().split()]
# matrix1 = [input().split() for _ in range(n)]
# input()
# [k2, m] = [int(num2) for num2 in input().split()]
# matrix2 = [input().split() for _ in range(k2)]
#
# k = k1
#
# matrix_res = [[int("0")]*m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         for r in range(k):
#             matrix_res[i][j] += int(matrix1[i][r]) * int(matrix2[r][j])
#
# for _ in range(n):
#     print(*matrix_res[_])



## 4.7.3 # возведение квадратной матрицы в степень m
#
# n = int(input())
# matrix1 = [input().split() for _ in range(n)]
# m = int(input())
#
# matrix_res = [[int("0")]*n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         for k in range(m):
#             matrix_res[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
#         # matrix[i][j] +=
# for _ in range(n):
#     print(*matrix_res[_])


## 6.2

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# b = 0
# for i in range(len(a)):
#     b += a[i]
# print(b)
# print(sum(a))

## 6.2.11
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)


## 6.2.12
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [tuples[i] for i in range(len(tuples)) if len(tuples[i]) > 0]
#
# print(non_empty_tuples)


## 6.2.13
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# for i in range(len(tuples)):
#     tuples[i] = list(tuples[i])
#     tuples[i][-1] = 100
#     tuples[i] = tuple(tuples[i])
# new_tuples = tuples
# print(new_tuples)

##6.3

# a = 'asdfasdfszdgasd'
# b = list(a)
# c = tuple(a)
# b.sort()
# print(b)
# print(tuple(sorted(c)))


## 6.3.4
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# a = [sum(i) / len(i) for i in numbers]
# print(a)


## 6.3.5
# a, b, c = int(input()), int(input()), int(input())
# x = (- b) / (2 * a)
# y = (4 * a * c - b ** 2) / (4 * a)
# coordinates = (x, y)
# print(coordinates)


## 6.3.6
# n = int(input())
# s = []
# for _ in range(n):
#     s.append(input().split())
#
# for _ in range(n):
#     print(*s[_])
# print()
#
# s1 = []
#
# for _ in range(n):
#     if int(s[_][1]) > 3:
#         s1.append(s[_])
#
# for _ in range(len(s1)):
#     print(*s1[_])


##6.3.7 упаковка и распаковка кортежей
# a = 1, 2, 3
# b = 5,
# print(a)
# print(b)
#
# c, d, e = a
# print(c)
# print(d)
# print(e)


##6.3.last.  Трибоначчи
# n = int(input())
# a = 1
# b = 1
# c = 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b, c = b, c, a + b + c



## 8.2.1
# m, n, k, x, y, z = [int(input()) for i in range(6)]
# s = z + m + n + k - x - y
# print(s)

## 8.2.2
# n, m, k, x, y, z, t, a = [int(input()) for i in range(8)]
# s1 = (k - n - m + t) + (n - k - m + t) + (m - k - n + t)
# s2 = x - (n - k - m + t) - (m - k - n + t) - t
# s0 = a - x - (k - n - m + t)
# print(s1)
# print(s2)
# print(s0)


# a = 'asbcdef'
# b = [1, 2, 3]
# c = (1, 2, 3)
# d = {1, 2, 3}
# e = {1: 2, 2: 3}
# f = 1, 23, 2
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

##8.4.3
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# summa = 0
# for i in numbers:
#     i ** 2
# print(sum(numbers))


##8.4.4
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# sorted_fruits = sorted(fruits, reverse=True)
# print(*sorted_fruits, sep="\n")

#8.4.7
# s1 = input()
# s2 = input()
# if set([str(i) for i in range(10)]) == set(s1 + s2):
#     print("YES")
# else:
#     print("NO")


#8.4.8
# if set(input()) == set(input()):
#     print("YES")
# else:
#     print("NO")

#8.4.9
# s = input().split()
# if set(s[0]) == set(s[1]) == set(s[2]):
#     print("YES")
# else:
#     print("NO")

## 8.5.1
# n = int(input())
# for i in range(n):
#     print(len(set(input().lower())))


## 8.5.2
# n = int(input())
# s = ''
# for i in range(n):
#     s += input().lower()
# print(len(set(s)))


## 8.5.3
# text = input()
# s = [word.lower().strip('.,;:-?!') for word in text.split()]
# print(len(set(s)))


## 8.5.3
# s = [int(i) for i in input().split()]
# print("NO")
# for i in range(1, len(s)):
#     if s[i] in s[:i]:
#         print("YES")
#     else:
#         print("NO")


## 8.6.

## НЕИЗМЕНЯЮЩИЕ МЕТОДЫ
# myset1 = {1, 2, 3, 4, 5}  #объедтнение множеств
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 | myset2
# print(myset3)
# myset1 = myset1.union(myset2)
# print(myset1)


# myset1 = {1, 2, 3, 4, 5}  #пересечение множеств
# myset2 = {3, 4, 6, 7, 8}

# myset3 = myset1.intersection(myset2)
# myset3 = myset1 & myset2
# print(myset3)


# myset1 = {1, 2, 3, 4, 5} #разность множеств #отличающиеся элементы одного множества
# myset2 = {3, 4, 6, 7, 8}
# #
# # myset3 = myset1.difference(myset2)
# myset3 = myset1- myset2
# print(myset3)


# myset1 = {1, 2, 3, 4, 5} #отличающиеся элементы обоих множеств
# myset2 = {3, 4, 6, 7, 8}
#
# # myset3 = myset1.symmetric_difference(myset2)
# myset3 = myset1 ^ myset2
# print(myset3)



## ИЗМЕНЯЮЩИЕ МЕТОДЫ  |=, &=, -=, ^=

# myset1 = {1, 2, 3, 4, 5}  #объедтнение множеств
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.update(myset2)
# print(myset1)


# myset1 = {1, 2, 3, 4, 5}  #объедтнение множеств
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.difference_update(myset2)
# print(myset1)


# myset1 = {1, 2, 3, 4, 5}  #объедтнение множеств
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.intersection_update(myset2)
# print(myset1)


# myset1 = {1, 2, 3, 4, 5}  #объедтнение множеств
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.symmetric_difference_update(myset2)
# print(myset1)


## 8.6.1
# s1, s2 = set(input().split()), set(input().split())
# print(len(s1 & s2))

## 8.6.2
# s1, s2 = set(input().split()), set(input().split())
# s = [int(i) for i in (s1 & s2)]
# print(*(sorted(s)))

## 8.6.3
# s1, s2 = set(input().split()), set(input().split())
# s = [int(i) for i in (s1 - s2)]
# print(*(sorted(s)))

## 8.6.4
n = int(input())
s = set([int(i) for i in list(input())])
my_set = s
for i in range(n - 1):
    s = set([int(i) for i in list(input())])
    my_set &= s
lst = list(my_set)
print(*(sorted(lst)))

# print(*sorted(lst))



