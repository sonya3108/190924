def move_zeros_to_end(lst):
    '''
    Функція переміщує всі нульові елементи (0 або 0.0) в кінець списку, зберігаючи порядок інших елементів.
    :param lst: список з елементами різних типів
    :return: новий список, де всі числові нулі знаходяться в кінці
    '''
    non_zero_elements = [x for x in lst if not (x == 0 and type(x) in [int, float])]
    zero_elements = [x for x in lst if x == 0 and type(x) in [int, float]]
    return non_zero_elements + zero_elements


print(move_zeros_to_end([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
print(move_zeros_to_end([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros_to_end([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


print(move_zeros_to_end(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros_to_end(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
print(move_zeros_to_end([1, None, 2, False, 1, 0]))
print(move_zeros_to_end(["a", "b"]))
print(move_zeros_to_end([2, 8]))
print(move_zeros_to_end([10]))
print(move_zeros_to_end([False]))
print(move_zeros_to_end([]))
