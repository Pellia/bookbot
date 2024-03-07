def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    count = get_count_words(book_text)
    print(book_text)
    print(f"The book contains {count} words")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_count_words(text):
    words = text.split()
    return len(words)

main()