#!/usr/bin/env python3
# coding : utf-8

__author__ = 'Sergei Krasavin'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).

easy_digit = input('Введите число ')
i = 0
while i < len(easy_digit):
    print(easy_digit[i])
    i += 1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.

first_digit = input('Введите что-нибудь ')
second_digit = input('Введите что-нибудь ещё ')
tmp = first_digit
first_digit = second_digit
second_digit = tmp
print('Новое значение первого числа: ',first_digit)
print('Новое значение второго числа: ',second_digit)
print('Это было первое число: ',second_digit)
print('Это было второе число: ',first_digit)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

access = None
age = int(input('Введите Ваш возраст:'))
if age >= 18:
    access = 1
    print ('Доступ разрешен')
else:
    access = 0
    print ('Извините, доступ разрешен ТОЛЬКО с 18 лет')
