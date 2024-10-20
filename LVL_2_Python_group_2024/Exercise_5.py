"""DICT - dictionary (collection, object,словник, колекція)"""
# {} - умовне позначення
# dict() - генератор словників

# dict_1 = {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu'}

# print(type(dict_1))
# print(isinstance(dict_1, dict))
# print(type(dict_1) is dict)

#Properties
#Змінювана структура
#__setitem__()
# dict_1['key_1'] = 111111111111
# dict_1['key_2'] = dict_1['key_2'] + 1000
# dict_1['key_3'] += "AAAAAAAAA"
# dict_1.__setitem__('key_1', 33333333333333)


#Унікальність ключів
# dict_1.update({'key_1' : 3563645343563453})

#Перераховуваність
# for key in dict_1:
#     print(key, dict_1[key])
#
# for key, values in dict_1.items():
#     print(key, values)

# dict_1 = {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu', 'key_1' : 45644546753}

# print(dict_1)

# KEYS : value
# int       {23423 : '1', -3653 : '654', 3563 : '5'}
# float     {-234.23 : '1', -3.653 : '654', 0.00003563 : '5'}
# bool      {True : '1', False : '654'}
# None      {None : '34g3g'}
#
# str       {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu'}
# tuple     {(12332,'serial#222',65654,4354.767) : 34534, (56,'serial#222',65,4354.767) : 425.34)

# key : VALUES
#ВСЕ ЩО ЗАВГОДНО

# dict_1 = {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu', 'key_4' : [25,34,536,45],
#  'key_5' : True, 'key_6' : {25,34,536,45}, 'key_6' : {True : '1', False : '654', 'key_1' : 3453},
#  'key_7' : len, 'key_8' : open('pyvenv.cfg', 'r')}

# print(dict_1)

#
# dict_1 = {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu', 'key_4' : [25,34,536,45],
#  'key_5' : True, 'key_6' : {25,34,536,45}, 'key_6' : {True : '1', False : '654', 'key_1' : 3453},
#  'key_7' : len, 'key_8' : open('pyvenv.cfg', 'r')}
#
# dict_1['key_4'].append(3453)
# dict_1['key_4'].sort()
#
# dict_1['key_6'][False] = 2222222222222222
# print(dict_1['key_7']('egeégeegerfuhfierojeuvheveuviehrvuievre'))

'''Basic fun'''
# dict_1 = {'key_1' : 34534, 'key_2' : 425.34, 'key_3' : 'rwfiwu'}
# dict_1.update({'key_5' : 453434, 'key_6' : -2545})
# dict_1.update({'key_1' :222222222222, 'key_2' : -22222222222})
# dict_1.update([('key_5' ,453434), ('key_1', -33333545)])
# dict_1.update(key_5 = 453434, key_1 = -33333545)

# print(dict_1.setdefault('key_5', 333333333333))
# print(dict_1.setdefault('key_1', 333333333333))

# dict_1.clear()
# dict_1.pop('key_2')
# dict_1.popitem()
# del dict_1['key_2']
# del dict_1

# print(dict_1.get('key_1', 33333333333333))
# print(dict_1.get('key_5',[1,2,3,4,5]))

# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
# print(dict_1)

"""Marathon_1 FFA"""
from random import randint, choice, choices
"""#1"""
# list_one_zero = [0,1] * 10
# print(list_one_zero)
'''#2'''
# def count_one_zero()->list:
#     '''
#     Функція повертає список з 20х елементів, елементи це 0 та 1 де 1ць завжди більше ніж 0
#     :return:  список з 20х елементів
#     '''
#     return [choices([0,1], (0.34, 0.66))[0] for i in range(20)]
#
# print(count_one_zero())
'''#3'''
# def div(divisor, lst:list)->int:
#     '''
#     Приймає дільник та список чисел, та повертає кількість елментів списка які діляться на дільник без остачі
#     :param divisor: дільник
#     :param lst: список чисел
#     :return: кількість елементів які діляться без остачі
#     '''
#     return len([el for el in lst if el % 2 == divisor])
#
# def many(lst : list)->bool:
#     '''
#     :param lst:
#     :return:
#     '''
#     return div(0, lst) > div(1, lst)

'''#4'''
# def lettertToList(text:str)->list:
#     '''
#     :param text:
#     :return:
#     '''
#     text = text.lower()
#     return list({ f'{let} - {text.count(let)}' for let in text if let.isalpha()})

'''#5'''
# def crypt(num:str)->str:
#     '''
#     :param num:
#     :return:
#     '''
#
#     return ''.join([str((int(dig) + 9) % 10) for dig in num])
'''#6'''
# def qeueTime(cust: list, num_c : int)->int:
#     '''
#     :param cust:
#     :param num_c:
#     :return:
#     '''
#     list_open_cas = [0] * num_c
#
#     for time in cust:
#         index_cas = list_open_cas.index(min(list_open_cas))
#         list_open_cas[index_cas] += time
#
#     return max(list_open_cas)
