# Марафон_2 Вершина Софія

# 1
my_dict = {3: 9, 134: 44}

new_key = 2
new_value = 30

my_dict[new_key] = new_value

print(my_dict)

# 2

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def merge_dicts(dic1, dic2, dic3):
    merged_dict = {**dic1, **dic2, **dic3}
    return merged_dict


result = merge_dicts(dic1, dic2, dic3)
print(result)

# 3

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check_key(d, key):
    return key in d


key_to_check = 5
result = check_key(d, key_to_check)

print(f"Ключ {key_to_check} {'присутній' if result else 'відсутній'} у словнику.")


# 4

def sum_dict_values(d):
    return sum(d.values())


dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}

total_sum = sum_dict_values(dict_1)
print(f"Сума всіх значень у словнику: {total_sum}")


# 6

def remove_by_key(d, key_to_remove):
    if key_to_remove in d:
        del d[key_to_remove]
    return d


dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}

key_to_remove = 'Radeon 6600 MSI'

updated_dict = remove_by_key(dict_1, key_to_remove)
print(updated_dict)


# 7
def apply_discount(d, discount_percentage):
    discounted_dict = {key: value * (1 - discount_percentage / 100) for key, value in d.items()}
    return discounted_dict


dict_1 = {
    'rtx 4090 Palit GR': 70000,
    'GeForce 1650 Super GIGABYTE': 7000.50,
    'rtx 3060Ti Asus': 16700,
    'Radeon 7900XTX Saphire': 50000,
    'Rtx 3050 PNY': 8000,
    'rtx 4080 Palit Gaming Pro': 56000,
    'Radeon 6600 MSI': 13000,
    'Radeon 6650 XFX': 14200,
}

discount_percentage = 12
discounted_prices = apply_discount(dict_1, discount_percentage)

print(discounted_prices)

# 11
from itertools import product


def letter_combinations(d):
    combinations = product(*d.values())

    result = [''.join(combination) for combination in combinations]
    return result


data = {'3': ['c', 'w'], '8': ['f', 'p']}

combinations = letter_combinations(data)
print(combinations)


# _9

def reverse_dict(d):
    reversed_dict = {}


    for key, value in d.items():
        if value in reversed_dict:
            reversed_dict[value].append(key)
        else:
            reversed_dict[value] = [key]

    for key in reversed_dict:
        if len(reversed_dict[key]) == 1:
            reversed_dict[key] = reversed_dict[key][0]
            return reversed_dict

d = {'ad': 6, 'da': 9, 'yy': 4, 'ff': 2, 'pq': 13, 'xw': 10, 'ju': 7}

r = reverse_dict(d)
print(r)
