def upper_string(s):
    """
    Возвращает входную строку заглавными буквами.
    Параметры:
    строка (str): Входная строка.
    Возвращается:
    str: Вводимая строка заглавными буквами.
    """
    return s.upper()


result = upper_string("davydov")
print(result)

def capital_letter(string):
    """
Заглавными буквами пишется первая буква каждого слова при вводе строки.
Параметры:
строка (str): Входная строка.
Возвращается:
str: Входная строка, в которой первая буква каждого слова пишется с заглавной буквы.
"""
    return ' '.join([word.capitalize() for word in string.split()])


result = capital_letter("davydov petr")
print(result)
