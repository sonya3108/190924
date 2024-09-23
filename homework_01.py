text = input("Введіть рядок: ")


cleaned_text = text.replace(' ', '').lower()


if cleaned_text == cleaned_text[::-1]:
    print("Це паліндром!")
else:
    print("Це не паліндром!")
