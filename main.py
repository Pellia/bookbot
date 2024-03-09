def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    # Report
    print("----- Begin report of books/frankenstein.txt -----")
    print(f"- The book contains {num_words} words -")
    print("\n")
    print("The book contains the following letters:")
    print(chars_dict)
    print("\n")
    print("----- End report -----")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()