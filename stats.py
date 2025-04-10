import string

def count_characters(s):
    return len(s.replace(" ", ""))

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    total_length = sum(len(word.strip(string.punctuation)) for word in words)
    return total_length / len(words)    
