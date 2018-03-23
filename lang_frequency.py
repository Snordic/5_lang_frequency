import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_txt:
        return file_with_txt.read()


def clear_characters(text):
    list_words = re.findall(r'[а-яa-z]+', text)
    return list_words


def get_most_frequent_words(data_for_search, number_words=10):
    counted_words = Counter(data_for_search).most_common(number_words)
    return counted_words


def print_word_repetitons(counted_words):
    for word, count in counted_words:
        print('{} => {}'.format(word, count))


def format_lower(text):
    return text.lower()


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        data_from_file = load_data(filename)
    except IndexError:
        print('Ошибка: Не добавлен файл для поиска!')
    except FileNotFoundError:
        print('Ошибка: Данный файл не существует!')
    else:
        text_lower = format_lower(data_from_file)
        list_words = clear_characters(text_lower)
        counted_words = get_most_frequent_words(list_words)
        print_word_repetitons(counted_words)
