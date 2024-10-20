from os import mkdir, makedirs, remove, rename, rmdir, listdir
from shutil import rmtree, copytree, copy

from posixpath import exists, abspath, isdir, isfile, getsize, getctime, getatime, getmtime
from datetime import datetime

'''ADDRESS'''
#ABSOLUTE(global) - адреса файла або іншого об'єкта фс яка починається з назви диска
#C:\Users\Adnistrator\Dowloads\input.txt
#C:\Users\Administrator\PycharmProjects\pythonProject\.venv\Exercise_6.py

#Local - адреса "місце" відліку якої розпочинається з адреси розташування файла з кодом
#Exercise_4.py
#omg/file_1.txt

'''lib os'''
# mkdir(r'C:\Users\Administrator\Downloads\UFO')
# address = r'C:\Users\Administrator\Downloads\UFO_1'
#
# mkdir(address)
# mkdir('UFO')

# makedirs('UFO/lol/red')

# rename('UFO', 'FLO')
# remove('Exercise_4(copy).py')

# rmdir('FLO') - Видаляє тільки порожні дерикторії

# print(listdir(r'C:\Users\Administrator\PycharmProjects\pythonProject\.venv'))

'''lib shutil'''
# rmtree('omg')

# copytree(r'C:\Users\Administrator\PycharmProjects\pythonProject\.venv', r'C:\Users\Administrator\Downloads\UFO_2')
# copy('Exercise_4.py', 'Scripts')

'''lib posixpath'''

# print(exists('OMG'))
# print(exists('Exercise_4.py'))
# if exists('''Exercise_55.py''') :
#     print('Так файл наявний')
# else:
#     print("Покищо файла не існує, але колись він зявиться")

# print(abspath('Exercise_4.py'))
# print(abspath('lol.py'))

# isdir() isfile()
# print(isdir('Exercise_4.py'))
# print(isdir('Lib'))
# print(isfile('Exercise_4.py'))

# print(getsize('Exercise_5.py') / 1024)

# print(datetime.fromtimestamp(getmtime('Exercise_4.py'))
# print(datetime.fromtimestamp(getctime('Exercise_4.py')))
# print(datetime.fromtimestamp(getatime('Exercise_4.py')))
'''TEXT'''
# with open('input.txt', 'r') as fl:
#     # print(fl.read())
#     str_text = fl.read()

# print(str_text[1:135])

#
# with open('input.txt', 'r', encoding='utf-8') as fl:
#     print(fl.read())

# with open('input.txt', 'a', encoding='utf-8') as fl:
#     fl.write('\nHolz 100')
#
# with open('input.txt', 'w', encoding='utf-8') as fl:
#     fl.write('\nHolz 100')