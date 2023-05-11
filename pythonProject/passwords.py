from random import choice
from time import sleep

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars1 = ''
chars = ''

quantity = int(input("Введите количество паролей: "))
length = int(input("Введите длину одного пароля: "))

a = input("Включать ли цифры 0123456789? да/нет: ").lower()
b = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ да/нет: ").lower()
c = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет: ").lower()
d = input("Включать ли символы !#$%&*+-=?@^_? да/нет: ").lower()
e = input("Исключать ли неоднозначные символы il1Lo0O? да/нет: ").lower()

if a == "да":
    chars1 += "0123456789"
if b == "да":
    chars1 += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if c == "да":
    chars1 += "abcdefghijklmnopqrstuvwxyz"
if d == "да":
    chars1 += "!#$%&*+-=?@^_"
if e == "да":
    for i in chars1:
        if i not in "il1Lo0O":
            chars += i
        chars1 = chars

def generate_password(lenghth, chars):
    password = ''
    for _ in range(length):
        password += choice(chars1)
    return password

for _ in range(quantity):
    sleep(0.5)
    print(generate_password(length, chars))











