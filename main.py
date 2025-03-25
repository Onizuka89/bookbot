from stats import get_num_words, count_characters, count_characters_sorted_by_frequency
import sys

def get_book_text(path:str):
    with open(path) as file:
        for line in file.readlines():
            print(line, end="")


def main():
    book_path=sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at {}".format(book_path))
    print("----------- Word Count ----------")
    get_num_words(book_path)
    print("--------- Character Count -------")
    #char_dict = count_characters("./books/frankenstein.txt")
    #print(char_dict)
    count_characters_sorted_by_frequency(book_path)
    print("============= END ===============")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()

