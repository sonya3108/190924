# 1
import re

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text


def count_words_by_case(text):
    words = re.findall(r'\b\w+\b', text)

    capitalized_count = 0
    lowercase_count = 0

    for word in words:
        if word[0].isupper():
            capitalized_count += 1
        elif word[0].islower():
            lowercase_count += 1

    return {'capitalized words': capitalized_count, 'lowercase words': lowercase_count}

text = read_file("C:/Users/Admin/Desktop/190924/LVL_2_Python_group_2024/input_1.txt")
result_elementary = count_words_by_case(text)
print("Elementary level result:", result_elementary)

# 2
from collections import Counter

def find_most_frequent_shortest_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    most_frequent_shortest_word = min(word_counts, key=lambda word: (len(word), -word_counts[word]))
    return most_frequent_shortest_word


result_intermediate = find_most_frequent_shortest_word(text)
print("Intermediate level result:", result_intermediate)

# 3
def replace_frequent_word_with_caps(text, word_to_replace):
    pattern = re.compile(r'\b' + re.escape(word_to_replace) + r'\b', re.IGNORECASE)
    updated_text = pattern.sub(word_to_replace.upper(), text)
    return updated_text

updated_text = replace_frequent_word_with_caps(text, result_intermediate)
print("Advanced level result:\n", updated_text)

