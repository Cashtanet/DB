from random import choice

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
     "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
     "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
     "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
     "Перспективы не очень хорошие", "Весьма сомнительно"]

def choices(list):
    choices = choice(list)
    return choices


print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Введи свое имя, друг: ")
print(f"Привет, {name}!")

s = input("Хочешь меня о чем-то спросить? Да/Нет: ").lower()


while s == "да":
    input("Задавай свой вопрос: ")
    print(choice(answers))
    s = input("Еще вопросы? Да/Нет: ").lower()
else:
    print("Ну тогда пока!")

