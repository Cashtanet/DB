import random


def random_1(n):
    a = random.randint(1, n)
    return a

def guessing():
    trying = 0
    count = 0
    a = random_1(n)

    while trying != a:
        trying = int(input("Введите вашу догадку: "))
        if trying in range(1, n + 1):
            if trying == a:
                count += 1
                print("Вы угадали!")
                print("Общее число попыток:", count)
                break
            elif trying > a:
                count += 1
                print("Число немного больше загаданного")
            else:
                count += 1
                print("Число немного меньше загаданного")
        else:
            print("Число вне диапазона!")


n = int(input("Введите количество чисел: "))
guessing()


print("Спасибо за игру! До новых встреч!")



