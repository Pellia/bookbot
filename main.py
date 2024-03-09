def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_sort_dict(chars_dict)

    # Report
    print(f"----- Begin report of {book_path} -----")
    print(f"- The book contains {num_words} words -")
    print("")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("")
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

def get_sort_dict(chars_dict):
    list_dict = []
    for char in chars_dict:
            list_dict.append({"char": char, "num": chars_dict[char]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def sort_on(dict):
    return dict["num"]

main()