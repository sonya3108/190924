# 1
as_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [x for x in as_list if x < 5]
print(result)

# 2
as_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ba_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(set(as_list) & set(ba_list))
print(result)


# 3
arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]
result = list(set(arr) & set(bar))
print(result)






