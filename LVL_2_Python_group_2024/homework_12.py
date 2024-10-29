is_palindrome = lambda s: s == s[::-1]

print(is_palindrome("radar"))
print(is_palindrome("hello"))

get_odd_numbers = lambda lst: list(filter(lambda x: x % 2 != 0, lst))


print(get_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


filter_by_average_length = lambda words: list(filter(lambda w: len(w) <= sum(map(len, words)) / len(words), words))


words = ["jabłko", "kaki", "winogonora", "bzoskiwinia", "arbuz"]
print(filter_by_average_length(words))
