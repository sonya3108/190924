# 1
def max_even(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return max(even_numbers) if even_numbers else None


lst = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
print(max_even(lst))

# 2
def top_3_max(lst):
    unique_elements = list(set(lst))
    unique_elements.sort(reverse=True)
    return unique_elements[:3]


lst = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]
print(top_3_max(lst))

# 3
def compare_even_odd(list1, list2):
    even_count = sum(1 for num in list1 if num % 2 == 0)
    odd_count = sum(1 for num in list2 if num % 2 != 0)
    return even_count > odd_count


list1 = [1, 10, 4, 13, 22, 10, 0, 100, 12, 14, 105]
list2 = [1, 1, 3, 13, 22, 5, 17]
print(compare_even_odd(list1, list2))

