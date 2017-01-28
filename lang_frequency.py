import chardet
import re
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file_handler:
        return (file_handler.read()).lower()
    
def detect_encoding(file_path):
    with open(file_path, 'rb') as file_handler:
        encoding = chardet.detect(file_handler.readline())
        return encoding['encoding']

def get_split_text(text_content):
    return re.findall('\w+', text_content)

def get_word_frequencies(split_text):
    unic_words = set(split_text)
    number_words = len(split_text)
    words_frequency = [(word, split_text.count(word) / number_words) \
                       for word in unic_words]
    return words_frequency

def get_most_frequent_words(word_frequencies, number_of_words=20):
    most_frequent_words = [word for word, value in \
                           sorted(word_frequencies, key=lambda x: -x[1])]
    return most_frequent_words[:number_of_words]


if __name__ == '__main__':
    file_path = input('Enter path of file: ')
    text = load_data(file_path)
    split_text = get_split_text(text)
    word_frequencies = get_word_frequencies(split_text)
    most_frequent_words = get_most_frequent_words(word_frequencies)
    print(most_frequent_words)
