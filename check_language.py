import re

def count_letters(text, pattern):
    return len(re.findall(pattern, text))

def check_text_language(text):
    # Проверяем наличие латинских букв (a-zA-Z) в тексте
    latin_pattern = re.compile(r'[a-zA-Z]')

    # Проверяем наличие кириллических букв (а-яА-Я) в тексте
    cyrillic_pattern = re.compile(r'[а-яА-Я]')

    # Считаем количество латинских и кириллических букв
    latin_count = count_letters(text, latin_pattern)
    cyrillic_count = count_letters(text, cyrillic_pattern)

    if latin_count > 0 and cyrillic_count > 0:
        if latin_count > cyrillic_count:
            return "en"
        else:
            return "uk"
    elif latin_count > 0:
        return "en"
    elif cyrillic_count > 0:
        return "uk"
    else:
        return "none"

