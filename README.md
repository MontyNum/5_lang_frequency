# The most frequent words

This script returns 20 (by default) the most frequent words of a text file.

**load_data(***filepath***)** 

    Open file.txt and returns a corresponding file object

**get_split_text(***text_content***)**

    Split any text on words. Returns a list of the words which contain in our text file.
    
**get_word_frequencies(***split_text***)**

    Return a list of the words and its frequencies of using in the text.

**get_most_frequent_words(***word_frequencies, number_of_words=20***)**

    Return 20 (by default) the most frequent words of interesting text.
    
# Usage

Enter the path of the interesting text file:

    file_path = 'c://file_derectory//file_name.txt'
    
Load the data:

    text_content = load_data(file_path)
    
Split the text on words:

    split_text = get_split_text(text_content)
    
Calculate word frequencies:

    word_frequencies = get_word_frequencies(split_text)
    
Get the most frequent words of the text:

    most_frequent_words = get_most_frequent_words(word_frequencies)
    
