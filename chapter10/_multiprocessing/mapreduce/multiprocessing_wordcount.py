"""
В следующем примере класс SimpleMapReduce используется для подсчета слов
в файлах на языке разметки reStructuredText (расширение .rst), содержащих текст
данного раздела, с учетом того, что некоторые элементы разметки игнорируются.
"""
import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce


def file_to_words(filename):
    """Прочитать файл, и вернуть последовательность значений (число вхождений слов)
    (map_func)
    """
    STOP_WORDS = {'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if', 'in',
                  'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the', 'to', 'with'}
    TR = str.maketrans({
        p: ' '
        for p in string.punctuation
    })
    print(f'{multiprocessing.current_process().name} reading {filename}')
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            # Пропуск комментариев
            if line.lstrip().startswith('..'):
                continue
            line = line.translate(TR)  # отечение знаков пунктуации
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output


def cound_words(item):
    """Преобразовыввать сгруппированные данные для слова в кортеж,
    содержащий слово и число вхождений.
    (reduce_func)
    """
    word, occurences = item
    return (word, sum(occurences))


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.py')
    mapper = SimpleMapReduce(file_to_words, cound_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print('\nTOP 20 WORDS BY FREQUENCY\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print('{word:<{len}}: {count:5}'.format(
            len=longest + 1,
            word=word,
            count=count)
        )
