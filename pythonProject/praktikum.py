# bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
# for i in range(len(bremen_musicians)):
#     print(bremen_musicians[i])

#
# def check(i, b):
#     check = (i == b)
#     print(check)
#
# check(1,1)


# # Объявите функцию rooms_equal() с параметрами room_size и room_list
# def rooms_equal(room_size, room_list):
#     # Перенесите следующий код в тело функции, которую вы объявили
#     count = 0
#
#     for room in room_list:
#         if room == room_size:
#             count += 1
#
#
#     print('Комнат площадью', room_size, 'кв.м:', count)
#
# # Следующий код не изменяйте и не переносите в тело функции
# flat = [
#     5.55, 22.19, 7.78, 26.86, 5.55,
#     29.84, 22.19, 5.55, 16.85, 4.52
# ]
#
# hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
#
# rooms_equal(5.55, flat)
# # Добавьте ещё один вызов функции rooms_equal()
# # Передайте в функцию искомую площадь - 9.2 кв.м и список hut
# rooms_equal(9.2, hut)


# may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25,
#             17, 19]
# may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23,
#             18, 22, 23, 11]
#
#
# def comfort_count(temperatures):
#     # Напишите код функции
#     count = 0
#     for day in temperatures:
#         if day in range(22, 27):
#             count += 1
#     print("Количество тёплых дней в этом месяце:", count)
#
#
# # Дальше код не меняйте
# comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
# comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.



# def func_one():  #рекурсия(бесконечный цикл)
#     print('Раз')
#     func_two()
#
# def func_two():
#     print('Два')
#     func_one()
#
# func_one() # Вызываем функцию func_one()


#
# lst = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7]
# s = set(lst)
# print(s)


# def print_valid_cities(a, b):
#     c = a.difference(b)
#     # Вместо этого многоточия напишите код функции, она должна
#     # принимать и обрабатывать аргументы all_cities и used_cities,
#     # а затем печатать результат в нужном формате
#
# all_cities = {
#     'Абакан',
#     'Астрахань',
#     'Бобруйск',
#     'Калуга',
#     'Караганда',
#     'Кострома',
#     'Липецк',
#     'Новосибирск'
# }
#
# used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}
#
# print_valid_cities(all_cities, used_cities)



# def get_together_games(a, b):
#     for i in a:
#         if i in b:
#             print("👾", i)
#
# anfisa_games = [
#     'Online-chess',
#     'Города',
#     'DOOM',
#     'Крестики-нолики'
# ]
# alisa_games = [
#     'DOOM',
#     'Online-chess',
#     'Города',
#     'GTA',
#     'World of tanks'
# ]
# # Вызовите функцию со списками игр в качестве параметров
# get_together_games(anfisa_games, alisa_games)


# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return 'У тебя ' + str(count) + ' друзей.'
#
#
#     elif query == 'Кто все мои друзья?':
#         friends_string = ''
#
#         for i in DATABASE:
#             friends_string += i + " "
#         return friends_string
#
#     elif query == 'Где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         string = ''
#         for k in unique_cities:
#             string += k + ' '
#         return string
#
#     else:
#         return '<неизвестный запрос>'
#
# # Не изменяйте следующий код
# print('Привет, я Анфиса!')
# print(process_anfisa('Сколько у меня друзей?'))
# print("Твои друзья:", process_anfisa('Кто все мои друзья?'))
# print(f"Твои друзья в городах: {process_anfisa('Где все мои друзья?')}")





# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }


# # Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# # в зависимости от того, какое число передано в аргументе friends_count
# def format_friends_count(friends_count):
#     if friends_count == 1:
#         return '1 друг'
#     elif 2 <= friends_count <= 4:
#         return f'{friends_count} друга'
#     else:
#         return f'{friends_count} друзей'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         # Вызовите функцию format_friends_count() и передайте в неё count.
#         # Отредактируйте строку ниже: в ней должно использоваться выражение,
#         # которое вернёт функция format_friends_count()
#         return f'У тебя {format_friends_count(count)}.'
#
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_query(query):
#     lis = query.split(', ')
#     if lis[0] == 'Анфиса':
#         return process_anfisa(" ".join(lis[1:]))
#     else:
#         return process_friend(lis[0], " ".join(lis[1:]))
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         if 'ты где?' in query:
#             return f'{name} в городе {DATABASE[name]}'
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# print('Привет, я Анфиса!')
# print(process_query('Анфиса, сколько у меня друзей?'))
# print(process_query('Анфиса, кто все мои друзья?'))
# print(process_query('Анфиса, где все мои друзья?'))
# print(process_query('Анфиса, кто виноват?'))
# print(process_query('Соня, ты где?'))
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?'))
#
#
#
# # Дальше следует код, вызывающий вашу функцию; не изменяйте его:
# queries = [
#     'Анфиса, сколько у меня друзей?',
#     'Андрей, ну где ты был?',
#     'Андрей, ну обними меня скорей!',
#     'Анфиса, кто все мои друзья?'
# ]







# from random import choice
#
# def find_a_present(prizes):
#     return choice(prizes)
#
# print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
# print(find_a_present(['мяч', 'чебурашка', 'лосяш']))
#
#
# import random as r
#
# # Теперь к библиотеке random нужно обращаться только через псевдоним r:
# print(r.randint(0, 100)) # Случайное целое число от 0 до 100




#
# import datetime as dt
#
# # Взлёт: 1961 год, 12 апреля, 9 часов утра, 7 минут
# start_time = dt.datetime(1961, 4, 12, 9, 7, 0)
#
# print('Уже', start_time, 'Поехали!')
#
#
#
# import datetime as dt
#
# start_day = dt.datetime(1961, 4, 12)
#
# print(start_day)
#
#
# import datetime as dt
#
# start_time = dt.datetime(1961, 4, 12, 9, 7, 0)
#
# # Дата и время посадки: 1961 год, 12 апреля, 10 часов, 55 минут
# landing_time = dt.datetime(1961, 4, 17, 18, 55, 0)
#
# print(landing_time - start_time)





# import datetime as dt
#
# # Как и раньше - определяем текущее время UTC
# utc_time = dt.datetime.utcnow()
#
# # Создаём промежуток времени в три часа
# period = dt.timedelta(hours=3)
#
# # И прибавляем к значению времени по UTC поправку в три часа:
# moscow_time = utc_time + period
#
# # Печатаем
# print(moscow_time)





# import datetime as dt
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
# def what_time(city):
#     delta = dt.timedelta(hours = UTC_OFFSET[city])
#     return dt.datetime.utcnow() + delta
#     # Напишите код тела функции;
#     # она должна вернуть текущее время в городе city
#
# print(what_time('Казань'))
# print(what_time('Пермь'))
# print(what_time('Калининград'))







# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
# import datetime as dt
# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f_time
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         return f'У тебя {format_count_friends(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if city in UTC_OFFSET:
#                 return 'Там сейчас ' + str(what_time(city))
#         else:
#             return '<неизвестный запрос>'
#
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     elements = query.split(', ')
#     if elements[0] == 'Анфиса':
#         return process_anfisa(elements[1])
#     else:
#         return process_friend(elements[0], elements[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
# runner()








# import urllib.parse
#
#
# url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
#
# # чтобы вычленить текст вопроса
# # разбейте строку по знаку = и возьмите
# # второй элемент получившегося списка
# question = url.split('=')[1] # сохраните его в переменной question
#
# # напечатайте на экран запрос в расшифрованном виде
# print(urllib.parse.unquote(question)) # ваш код здесь



#
# import requests
#
# # Отправляем GET-запрос:
# response = requests.get('http://info.cern.ch/')
#
# print(response.text)  # Печатаем код запрошенной страницы.





#
# import requests
#
# url = 'http://wttr.in/?0T'
#
# response = requests.get(url)  # выполните HTTP-запрос
#
# print(response.text)  # напечатайте текст HTTP-ответа



#
# import requests
#
# url = 'https://wttr.in'
#
# weather_parameters = {
#     '0': '',
#     'T': '',  # удалите этот параметр
#     'M': '',
# }
#
# request_headers = {
#     'Accept-Language': 'ru'# заполните словарь с заголовками
# }
#
# # не забудьте передать параметры и заголовки в http-запрос
# # через аргументы `params` и `headers` функции get()
# response = requests.get(url, headers=request_headers, params=weather_parameters)
# print(response.text)





# # вот функция, которая может выбросить исключение
# def calc_share(apples, friends):
#     # от строки откусываем число и приводим к типу int
#     friends_number = int(friends.split()[0])
#     return apples/friends_number
#
# # есть 17 яблок
# apples = 17
#
# # будем считать, сколько достанется каждому другу
# # вызовем функцию calc_share() для разных наших знакомых,
# # с различным числом друзей
# for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
#         try:
#                 print('Каждому достанется по', calc_share(apples, friends), 'яблока')
#         except ZeroDivisionError:
#                 print('На ноль делить нельзя.')
#         except ValueError:
#                 print(f'Из строки "{friends}" не получилось достать число.')





# import requests
#
# cities = [
#     'Омск',
#     'Калининград',
#     'Челябинск',
#     'Владивосток',
#     'Красноярск',
#     'Москва',
#     'Екатеринбург'
# ]
#
#
# def make_url(city):
#     return f'http://wttr.in/{city}'
#
#
# def make_parameters():
#     params = {
#         'format': 2,  # погода одной строкой
#         'M': ''  # скорость ветра в "м/с"
#     }
#     return params
#
#
# def what_weather(city):
#     try:
#         response = requests.get(make_url(city), params=make_parameters())
#     except requests.ConnectionError:
#         return '<сетевая ошибка>'
#     if response.status_code == 200:
#         return response.text
#     else:
#         return '<ошибка на сервере погоды>'
#     # Напишите тело этой функции.
#     # Не изменяйте остальной код!
#
#
# print('Погода в городах:')
# for city in cities:
#     print(city, what_weather(city))












import datetime as dt
import requests

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
    }


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            return what_weather(city)
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Антон, как погода?'
    ]
    for query in queries:
        print(query, '-', process_query(query))
#
# runner()

