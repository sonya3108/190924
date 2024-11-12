"""#7"""
def count_vowels_letters(text:str, *, isvowel:bool = True)->int:
    '''
    Функція обчислює кількість голосних літер або приголосних
    :param text: текст для пошуку
    :param isvowel: логічний параметр який налаштовує що саме шукати,
     якщо True то рахувати тільки голосні літери,
     або інакше якщо False то шукати тільки приголосні
    :return: кількість знайдених літер
    '''
    return len([sym for sym in text if (sym in 'auioeуеїаоієияю') == isvowel and sym.isalpha()])

def most_popular(text:str)->list:
    '''
    Функція приймає текст для обробки
    :param text: основний текст для пошуку найпопопулярніших літер
    :return: одну або три найпопулярніших літери, в залежності від кількості голосних чи приголосних літер
    '''

    text = text.lower()

    vow = count_vowels_letters(text)
    cons = count_vowels_letters(text, isvowel=False)
    if vow > cons:
        dict_vowels_letters = {letter : text.count(letter) for letter in text if
                               letter in 'auioeуеїаоієияю' and letter.isalpha()  }
        return sorted(dict_vowels_letters, key=dict_vowels_letters.get)[-3:]
    elif vow < cons:
        dict_vowels_letters = {letter: text.count(letter) for letter in text if
                               not letter in 'auioeуеїаоієияю' and letter.isalpha()}
        return sorted(dict_vowels_letters, key=dict_vowels_letters.get)[-1]


with open('input_8.txt', 'r', encoding='utf-8') as fl:
    str_1 = fl.read()

print(most_popular(str_1))

with open('output.txt', 'w', encoding='utf-8') as fl:
    fl.write(f'most popular letter(s) is: {most_popular(str_1)}')




