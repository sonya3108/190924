# Марафон_1 Вершина Софія

# 1
def generate_zero_one_list(n):
    """
    Функція генерує список з рівною кількістю 0 і 1.
    Кількість елементів в списку = 2 * n.

    :param n: кількість пар (0, 1)
    :return: список у вигляді [0, 1, 0, 1, ..., 0, 1]
    """
    return [i % 2 for i in range(2 * n)]

n = 3
result = generate_zero_one_list(n)
print(result)

# 2
import random


def generate_unordered_zero_one_list():
    """
    Функція генерує список з 20 елементів, де елементами є 0 і 1,
    і кількість одиниць завжди більше за кількість нулів хоча б на одну одиницю.

    :return: список із 20 елементів (0 і 1)
    """
    ones_count = random.randint(14, 18)
    zeros_count = 20 - ones_count

    result = [1] * ones_count + [0] * zeros_count
    random.shuffle(result)
    return result


generated_list = generate_unordered_zero_one_list()
print(generated_list)
print(f"Кількість 4: {generated_list.count(1)}, Кількість 3: {generated_list.count(0)}")


# 3
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return "Парних більше" if even_count > odd_count else "Непарних більше" if odd_count > even_count else "Однаково"


numbers = [1, 2, 36, 18, 12, 69, 74, 81, 13, 11]
result = count_even_odd(numbers)
print(result)

# 4
def count_letters(text):
    text = text.lower()
    unique_letters = set(text)
    return [f"{letter} - {text.count(letter)}" for letter in unique_letters if letter.isalpha()]


result = count_letters('AAAbbabababaBBBababbb')
print(result)

# 5
def encrypt_phone_number(phone_number):
    encrypted_number = ''.join([str((int(digit) + 9) % 10) for digit in phone_number if digit.isdigit()])
    return encrypted_number


phone_number = "09765208302"
encrypted = encrypt_phone_number(phone_number)
print(encrypted)

# 6
import heapq


def total_queue_time(clients, num_cashes):
    if len(clients) <= num_cashes:
        return max(clients)


    cashes = [0] * num_cashes
    heapq.heapify(cashes)


    for client_time in clients:

        min_cash = heapq.heappop(cashes)

        heapq.heappush(cashes, min_cash + client_time)


    return max(cashes)



clients = [3, 9, 2, 6, 3, 1, 7]
num_cashes = 3
print(total_queue_time(clients, num_cashes))


# 7
def count_key_presses(s: str) -> int:
    key_presses = 0
    caps_lock_on = False

    for char in s:
        if char.islower():
            if caps_lock_on:
                key_presses += 1
                caps_lock_on = False
            key_presses += 1  #

        else:
            if not caps_lock_on:
                key_presses += 1
                caps_lock_on = True
            key_presses += 1

    return key_presses


print(count_key_presses("aaa"))
print(count_key_presses("a"))
print(count_key_presses("A"))
print(count_key_presses("AaA"))



