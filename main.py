def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = get_count_words(book_text)
    letter_count = get_count_letters(book_text)
    print(book_text)
    print(f"The book contains {word_count} words")
    print(letter_count)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_letters(text):
    letter_list = {}
    for char in text:
        letter = char.lower()
        if letter in letter_list:
            letter_list[letter] += 1
        else:
            letter_list[letter] = 1
    return letter_list

main()