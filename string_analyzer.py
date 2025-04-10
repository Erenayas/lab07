from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length,
)

def main():
    sentence = input("Enter a sentence: ")

    reversed_sentence = reverse_string(sentence)
    capitalized_sentence = capitalize_words(sentence)
    print(f"Reversed Sentence: {reversed_sentence}")
    print(f"Capitalized Sentence: {capitalized_sentence}")

   
    cleaned_sentence = remove_punctuation(sentence)
    char_count = count_characters(cleaned_sentence)
    word_count = count_words(cleaned_sentence)
    print(f"Character Count (excluding spaces): {char_count}")
    print(f"Word Count: {word_count}")


    avg_word_length = average_word_length(cleaned_sentence)
    print(f"Average Word Length: {avg_word_length:.2f}")

if __name__ == "__main__":
    main()
