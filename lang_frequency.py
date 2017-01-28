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
    
def read_data(file_txt):
    return file_txt.lower()

def get_split_text(txt_content):
    return re.findall('\w+', txt_content)

def get_words_frequency(split_text):
    unic_words = set(split_text)
    number_words = len(split_text)
    words_frequency = [(word, split_text.count(word) / number_words) \
                       for word in unic_words]
    return words_frequency

def get_most_frequent_words(words_frequency, frequent_words_number=20):
    most_frequent_words = [word for word, value in \
                           sorted(words_frequency, key=lambda x: -x[1])]
    return most_frequent_words[:frequent_words_number]


if __name__ == '__main__':
    file_path = input('Enter path of file: ')
    text = load_data(file_path)
    split_text = get_split_text(text)
    words_frequency = get_words_frequency(split_text)
    most_frequent_words = get_most_frequent_words(words_frequency)
    print(most_frequent_words)
