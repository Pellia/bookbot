def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    print(book_text)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()