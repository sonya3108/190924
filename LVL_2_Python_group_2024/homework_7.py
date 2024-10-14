import re
from collections import Counter

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


# Уровень Elementary
def elementary_analysis(text):
    text_lower = text.lower()
    letters = re.findall(r'[a-zа-я]', text_lower)
    digits = re.findall(r'\d', text_lower)
    whitespaces = re.findall(r'\s', text_lower)
    other = re.findall(r'[^\w\s]', text_lower)

    result = {
        'letters': len(letters),
        'digits': len(digits),
        'whitespaces': len(whitespaces),
        'other': len(other)
    }
    return result


# Уровень Intermediate
def intermediate_analysis(text):
    text_lower = text.lower()

    vowels_set = set("jdgugrbtфів")
    consonants_set = set("алпршгапркущпрнкупjfhgukdh")

    letters = re.findall(r'[a-zа-я]', text_lower)

    vowels = [letter for letter in letters if letter in vowels_set]
    consonants = [letter for letter in letters if letter in consonants_set]

    result = {
        'vowels': len(vowels),
        'consonants': len(consonants)
    }
    return result


# Уровень Advanced
def advanced_analysis(text):
    text_lower = text.lower()

    vowels_set = set("рлврппęąćhthhfg")
    consonants_set = set("gdhuifhrgkdhduенгаупагспус")

    letters = re.findall(r'[a-zа-я]', text_lower)

    vowels = [letter for letter in letters if letter in vowels_set]
    consonants = [letter for letter in letters if letter in consonants_set]

    if len(consonants) > len(vowels):
        most_common_consonant = Counter(consonants).most_common(1)[0][0]
        result = f"The most frequent consonant: {most_common_consonant}"
    else:

        most_common_vowels = [item[0] for item in Counter(vowels).most_common(3)]
        result = f"The three most frequent vowels: {', '.join(most_common_vowels)}"


    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(result)

    return result



text = read_file("C:/Users/Admin/Desktop/190924/LVL_2_Python_group_2024/input_8.txt")


elementary_result = elementary_analysis(text)
print("Elementary result:", elementary_result)


intermediate_result = intermediate_analysis(text)
print("Intermediate result:", intermediate_result)


advanced_result = advanced_analysis(text)
print("Advanced result:", advanced_result)