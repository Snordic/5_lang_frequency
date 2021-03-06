# Описание проекта

Данный скрип составляет список самых частотных слов в файле.

# Состав проекта

1) `load_data`
 Функция возвращающее данные полученные с файла.

2) `convert_text_to_list`
 Функция на вход который подаются данные с файл. При помощи регулярных выражении происходит "очистка данных" от не нужных чисел, знаков, пробелов. Возвращает список содержащий только слова.

3) `get_most_frequent_words`
Функция на вход которой подается "очищеные данные" для поиска наиболее частотных слов. Возвращает список данных с количеством повтора.

4) `print_word_repetitons` 
Функция выводящее в консоль наиболее частотные слова с количеством повтора.

# Как использовать

Необходимо добавить проект:

```python
import lang_frequence
```
 
Запустить функцию с путем до файла:

```python
lang_frequence.main('you_file')
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5. Необходимо скачать файл для работы.

Запуск на Linux:

```bash

$ python lang_frequence.py <path to file> # possibly requires call of python3 executive instead of just python


и => 25
в => 20
на => 9
а => 6
мы => 5
все => 5
с => 5
пусть => 5
что => 5
будет => 4
```

Запуск на Windows происходит аналогично.


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
