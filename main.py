def main():
    book_location = "books/frankenstein.txt"
    book_contents = get_book_text(book_location);
    print(book_contents)


    print(f"--- Begin report of {book_location} ---")
    print(f"{count_words_in_text(book_contents)} words found in the book")
    dictionary = count_characters_in_text(book_contents)
    my_list = make_entry_list(dictionary)
    print()
    pretty_print(my_list)
    print("--- End report ---")


def sort_on_count(dictionary):
    return dictionary["count"]


def make_entry_list(dictionary):
    my_list = []
    for key in dictionary.keys():
        if key >= 'a' and key <= 'z':
            my_list.append({"character": key, "count": dictionary.get(key, 0)})

    
    my_list.sort(reverse=True, key=sort_on_count)
    return my_list


def pretty_print(list):
    for entry in list:
        print(f"The '{entry['character']}' character was found {entry['count']} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words_in_text(book_text):
    words = book_text.split()
    return len(words)


def count_characters_in_text(book_text):
    dictionary = {}
    for char in book_text:
        char = char.lower()
        try:
            dictionary[char] += 1
        except KeyError as e:
            dictionary[char] = 1

    return dictionary


if __name__ == "__main__":
    main()
