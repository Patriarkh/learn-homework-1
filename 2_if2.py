"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def check(first, sec):
    if not isinstance(first, str) and not isinstance(sec, str):
        return("0")
    elif first == sec:
        return("1")
    elif first != sec and len(first) > len(sec):
        return("2")
    elif first != sec and sec == "learn":
        return(3)
    
print(check("df", "df"))
print(check("dff", "df"))
print(check("df", "learn"))