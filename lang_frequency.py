import re
from collections import Counter
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file_with_txt:
            data_form_file = file_with_txt.read()
    except FileNotFoundError:
        print('Ошибка: Данный файл не существует!')
        return None
    else:
        return data_form_file.lower()


def clear_characters(text):
    list_words = re.findall(r'[а-яa-z]+', text)
    return list_words


def get_most_frequent_words(data_for_search, number_words=10):
    counted_words = Counter(data_for_search).most_common(number_words)
    return counted_words


def print_word_repetitons(counted_words):
    for key, value in counted_words:
        print('{} => {}'.format(key, value))


def main(filepath):
    data_from_file = load_data(filepath)
    if data_from_file:
        list_words = clear_characters(data_from_file)
        counted_words = get_most_frequent_words(list_words)
        print_word_repetitons(counted_words)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Ошибка: Не добавлен файл для поиска!')
    else:
        main(filename)
