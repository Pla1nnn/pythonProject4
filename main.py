
str = str()

while True:
    n = input()
    if n == "stop":
        print(str,"Конец программы")
        break
    else:
        str = str + " " + n
        print(str)
def prog1 ():
    n = input()
    while True:
        if "ф" in n:
            print("Ого! Это редкое слово")
        else:
            print("Не редкое")
            break
def prog2()
    from random import *
    a = 0
    b = 0
    x = int()
    y = int()
    while a < 3:
        x = randint(1, 10)
        y = randint(1, 10)
        print(x, "+", y)
        n = int(input("Введите ответ:"))
        if (n == x + y):
            print("Правильно")
            b = b + 1
        else:
            a = a + 1
            print("Ошибка!")
            print("Осталось попыток:", 3 - a)
    print("Игра закончена. Кол-во верных ответов:", b)


prog1()
prog2()