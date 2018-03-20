import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_txt:
        data_form_file = file_with_txt.read()
    return data_form_file.lower()


def clear_characters(data_for_clearning):
    data_clear = re.findall(r'[а-яa-z]+', data_for_clearning)
    return data_clear


def get_most_frequent_words(data_for_search):
    found_items = Counter(data_for_search).most_common(10)
    print(found_items)
    return found_items


def print_word_repetitons(filepath):
    data_from_file = load_data(filepath)
    data_clear = clear_characters(data_from_file)
    found_items = get_most_frequent_words(data_clear)
    for key, value in found_items:
        print('%s => %s' % (key, value))


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        print_word_repetitons(filename)
    except IndexError:
        print('Ошибка: Не добавлен файл для поиска!')
