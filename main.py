'''Задание 1'''
import random

for i in range(5, 0, -1):
    print(i)
print("Расчёт окончен")

'''Задание 2'''
a = 3
for b in range(1, 11):
    print(a * b, end ='\n')
print()

"""Задание 3"""
N = random.randint(1,10)
A = int(input('Попытка 1:'))
if A > N:
    print('Бери меньше')
if A < N:
    print('Бери больше')
if A == N:
    print('Угадал')


A2 = int(input('Попытка 2:'))
if A2 > N:
    print('Бери меньше')
if A2 < N:
    print('Бери больше')
if A2 == N:
    print('Угадал')


A3 = int(input('Попытка 3:'))
if A3 > N:
    print('Бери меньше')
if A3 < N:
    print('Бери больше')
if A3 == N:
    print('Угадал')
if A3 != N:
    print('Не повезло, попробуй в следующий раз')

"""Задание 4"""
for row in range(1, 10):
    for col in range(1, 10):
        print(row * col,  end='\t' )
    print()

"""Задание 5"""
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
a = input('введите текс(на инглише):')
key = int(input('Введите ключ:'))
a = a.lower()
b = ''
for letter in a:
    c = alphabet.find(letter)
    d = c + key
    if  letter in alphabet:
        b = b + alphabet[d]
    else:
        b = b + letter
print('Зашифрованный текст:', b)
