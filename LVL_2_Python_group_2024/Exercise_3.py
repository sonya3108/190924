"""Funtion"""
# def bubble_sort(lst, key=None):
#     # for i in range(len(lst)):
#     #     for j in range(len(lst) - 1 - i):
#     #         if key and key(lst[j]) > key(lst[j + 1]):
#     #             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     #         elif key == None and lst[j] > lst[j + 1]:
#     #             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
# list_1 = [423,534,65,3546,45,76,4357,45,67457856,8]
#
# list_1 = bubble_sort(list_1)
#
# print(list_1)
#
# pass
# print('wrfuhiwberuif')
#
# list_2 = ['ergertgh', 'etrh6y', 'yrtjhrthj', 'rtyjhrtjhrtjh', '1  4534 ','  erg45g']
#
# # for i in range(len(list_2)):
# #     for j in range(len(list_2) - 1 - i):
# #         if list_2[j] > list_2[j + 1]:
# #             list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]
# list_2 = bubble_sort(list_2)
#
# print(list_2)
#
#
# list_3 = ['ergertgh', 'etrh6y', 'yrtjhrthj', 'rtyjhrtjhrtjh', '1  4534 ','  erg45g']
#
# # for i in range(len(list_3)):
# #     for j in range(len(list_3) - 1 - i):
# #         if len(list_3[j]) > len(list_3[j + 1]):
# #             list_3[j], list_3[j + 1] = list_3[j + 1], list_3[j]
#
# list_3 = bubble_sort(list_3, key=len)
# print(list_3)
"""Arguments (parameters) - аргументи(параметри) функцій"""

'''Positional args - обов'язкові аргументи(параметри)'''
# def bubble_sort(lst, key=None):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst

'''Default values - значення зазамовченням або не обов'язкові аргументи'''
# def bubble_sort(lst, op, key=None,  reverse = True):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
    # print(lst)
    # print(f'{key=}')
# sorted()
# def bubble_sort(lst = [], op='LOL', key=None,  reverse = True):

# list_1 = ['wr34', 'rfef', 'ref', 'f4', '1','2435t453','34', '']
# print(bubble_sort(list_1, len))

"""* - як оператор іменованих параметрів"""
# print(sorted(list_1, key = len))
# def bubble_sort(lst, *, key=None,  reverse = True):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
#
# list_1 = ['wr34', 'rfef', 'ref', 'f4', '1', '2435t453', '34', '']

# print(bubble_sort(list_1, reverse = False, key = len))
# print(bubble_sort(list_1, key = len, reverse = False))
# print(bubble_sort(list_1, reverse = False))
# print(bubble_sort(list_1, key = len))
# print(bubble_sort(list_1))

'''* **  - оператори пакування та розпакування'''
# * - як розпакувальник
# list_1 = [4,56,54687,54678,7564,8,345,32]

# print(*list_1, sep='\n')
# print(*list_1, sep='-')

# str_1 = 'poligon'
# list_1 = [4,56,54687,54678,7564, str_1,8,345,32]
# list_1 = [4,56,54687,54678,7564, *str_1,8,345,32]
# list_1 = list(str_1)
# print(list_1)


# * - як пакувальник
# def fun_4(*args):
#     print(f'{args=}')
#
#
# fun_4(42,6456,452345,'wfh34','2089rye23890ry')

# print(max(234,65,45,345,36,45,76,4123,312,3,65,869,86,3,453))

# ** - як розпакувальник колекцій або словників

# dict_1 = {'key_1' : 234, 'key_2' : 346, 'key_3' : 6452}
# dict_2 = {'wfwer' : 2345235, **dict_1, 'grer': False}
# dict_2 = {'wfwer' : 2345235, 'grer': False}
# dict_2.update(dict_1)

# ** - як пакувальник в функціях
# def fun_5(**kwargs):
#     print(kwargs)


# fun_5(lol = 3435, ulog = 'fiuewryhf89w')
# print(dict_2)

# dict_1 = {'key_1' : 234, 'key_2' : 346, 'key_3' : 6452}
#
# dict_1.update(orfr = '3fgerger')
# print(dict_1)

'''ОБОВ'ЯЗКОВО ДО ОФОРМЛЕННЯ КОДУ А САМЕ КОЖНОЇ ФУНКЦІЇ'''
'''Recomendet types - рукомендована типізація'''

# def bubble_sort(lst:list, key:None = None,  reverse:bool = True):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst

# sorted()
"""DOC FUNCTION - (форматний) опис функції"""
# def bubble_sort(lst:list, key:None = None, reverse:bool = True):
#     '''
#     Сортування списку методом Бульбашки.
#     :param lst: головний параметр функції, список для сортування
#     :param key: додатковий параметр для налаштування характеру порівняння елементів при сортуванні
#     :param reverse: додатковий параметр для визначення напрямку сортування списка а саме за ЗРОСТАННЯМ або за СПАДАННЯМ.
#     :return: відсортований список.
#     '''
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1 - i):
#             if (key and key(lst[j]) > key(lst[j + 1])) or (key == None and lst[j] > lst[j + 1]):
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
# bubble_sort()

# sorted()