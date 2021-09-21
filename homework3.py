"""
Задание 1(5 - баллов):
Напишите программу, которая преобразует из значение температуры из Цельсия в Фарангейты.
Значние температуры в Цельсиях вводится пользователем
Формулу погуглите))
"""

#  BEGIN
t = int(input())
print(t*1.8+32)
#  END

"""
Задание 2(5 - балоов):
В python кроме стандартных операций ==, !=, <, >
есть еще операции
1. >= это больше или равно 2 >= 1 -> True, 2 >= 2 -> True, 2 >= 3 -> False
2. <= это меньше или равно 2 <= 3 -> True, 2 <= 2 -> True, 2 <= 1 -> False
Напишите программу, которая вычисляет модуль числа.
Модуль числа это такая математическая функция:
|x| = x, если x >= 0
|x| = -x, если x < 0
Число вводится пользоваетелем.
"""
#  BEGIN
x = int(input())
if x >= 0:
    print(x)
else:
    print(x * (-1))
#  END

"""
Задание 3(7 - баллов):
Напишите программу, которая считает функцию голосования.
Функция голосование это логическая функция f(x, y, z) от трех
логических(это значит они принимают значение либо True либо False) аргументов x, y, z
и вычисляется следющим образом:
f(x, y, x) = True, если ХОТЯ БЫ два из трех аргументов True, иначе она равна False
Пример: f(True, False, True) = True
В этом задании нужно считать три значение x, y, z.
0 будет отвечать за False
1 будет отвечать за True
И вывести на экран значение фукнции голосования от этих трех значений.
Пример взаимодействия:
0
1
1
>> True
Пример взаимодействия:
0
0
1
>> False
"""

#  BEGIN
x = int(input())
y = int(input())
z = int(input())

if x > 0 and y > 0 or x > 0 and z > 0 or y > 0 and z > 0:
    print("True")
else:
    print("False")
#  END

"""
Задание 4(7 - баллов):
Напишите программу, которая для введенного целого числа n считает значение
факториала  n!. n! = 1 * 2 * 3 * ... * n
"""

#  BEGIN
x = int(input())
a = 1
for i in range (1, x+1):
    a = a * i
print(a)
#  END


"""
Задание 5(8 - баллов):
Напишите программу, которая для введенного целого числа n считает значение произведения
всех четных чисел до n(n >= 2)включительно.
Пример: n = 6: 2 * 4 * 6 = 48
        n = 4: 2 * 4 = 8
        n = 2: 2
"""

#  BEGIN
n = int(input())
a = 1
for i in range (2, n+1, 2):
        a *= i
print(a)
#  END


"""
Задание 6(8 - баллов):
Напишите программу, которая для введененой строки считает количество символов латинской 'a' в ней
и печатает на экран
Вводится строка только в нижнем регистре
Пример: для "margarita" это выведется 3
        для "python is the best" выведется 0
"""

#  BEGIN
string = input()
x = 0
for c in string:
    if c == 'a':
        x+=1
print(x)
#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество гласных букв в ней
и печатает на экран. Гласными считаются: a, e, i, o, u, y
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 4 (a - 3, i - 1)
        для "python is the best" выведется 5 (y - 1, o - 1, i - 1, e - 2)
"""
#  BEGIN
string = input()
x = 0
for c in string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'u' or c == 'y' or c == 'o':
        x+=1
print(x)
#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество согласных букв в ней
и печатает на экран. В этой задаче будем считать, что строка не содержит пробелов.
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 5
"""
#  BEGIN
string = input()
x = 0
for c in string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'u' or c == 'y' or c == 'o':
        x+=1
print(len(string) - x)
#  END


"""
Задание 8(20 - баллов):
Напишите программу, которая для введененой строки печатает ее символы в обрамном порядке
Пример: для "margarita" выведется "atiragram"
        для "python is the best" выведется "tseb eht si nohtyp"
Вводится строка только в нижнем регистре
"""
#  BEGIN
string = input()
print(string[::-1])
#  END


"""
Задание 9(20 - баллов):
Напишите программу, которая для введенного целого числа n печатает такую вот пирамиду
1
2 2
3 3 3
4 4 4 4
....
n n n ... n
В последней строке n раз напечатали n
"""

#  BEGIN
n = int(input())
for i in range(1, n + 1):
    for x in range(i):
        print(i, end=" ")
    print(" ")
#  END