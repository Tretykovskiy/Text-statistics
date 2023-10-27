import string


def text_stat(filename):
    # Проверка на корректность имени файла
    if not isinstance(filename, str):
        return {"error": "Invalid filename"}

    try:
        with open(filename, "r") as file:
            text = file.read()
    except FileNotFoundError:
        return {"error": "File not found"}

    # Инициализация переменных для статистики
    letter_frequency = {}
    word_amount = len(text.split())
    paragraph_amount = text.count("\n")
    bilingual_word_amount = 0

    # Подсчет частоты использования букв
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

    # Подсчет доли слов, в которых встречается конкретная буква
    word_with_letter_ratio = {}
    for letter in letter_frequency:
        count = 0
        for word in text.split():
            if letter in word:
                count += 1
        ratio = count / word_amount
        word_with_letter_ratio[letter] = ratio

    # Подсчет количества слов, в которых одновременно встречаются буквы обоих алфавитов
    for word in text.split():
        contains_latin = False
        contains_cyrillic = False
        for letter in word:
            if letter in string.ascii_letters:
                contains_latin = True
            elif letter in string.ascii_uppercase + string.ascii_lowercase:
                contains_cyrillic = True
        if contains_latin and contains_cyrillic:
            bilingual_word_amount += 1

    # Формирование результирующего словаря
    result = {
        "word_amount": word_amount,
        "paragraph_amount": paragraph_amount,
        "bilingual_word_amount": bilingual_word_amount
    }
    for letter in letter_frequency:
        result[letter] = (letter_frequency[letter], word_with_letter_ratio[letter])

    return result


filename = "example.txt"
statistics = text_stat(filename)
print(statistics)
