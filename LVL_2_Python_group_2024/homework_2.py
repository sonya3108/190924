# 1
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = [x for x in list_1 if x < 5]
# print(result)

# 2
# list_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(set(list_2) & set(list_3))
# print(result)


# 3
def unique_common_elements(arr, bar):
    common_elements = set(arr).intersection(set(bar))

    result = sorted(common_elements, key=lambda x: (arr.index(x) if x in arr else bar.index(x)))

    return result


arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

result = unique_common_elements(arr, bar)
print(result)





























