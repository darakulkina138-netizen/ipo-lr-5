#darakulkina138-netizen
def analyze_string():
    text = input("Введите строку на русском языке: ")
    length = len(text)
    print(f"Длина строки: {length}")
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha() and ('а' <= char <= 'я' or 'А' <= char <= 'Я' or char in 'ёЁ'):
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"Количество гласных: {vowel_count}")
    print(f"Количество согласных: {consonant_count}")
analyze_string()
