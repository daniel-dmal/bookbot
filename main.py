from stats import get_words_number, get_char_count, sort_dict
import sys
def get_book_text (file):
        with open(file) as f:
                return f.read()

def main():
        if (len(sys.argv) != 2 ):
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
                return
        path = sys.argv[1]
        book_text = get_book_text(path)
        number_of_words = get_words_number(book_text)
        char_count = get_char_count(book_text)
        sorted_dict = sort_dict(char_count)
        print("-------- Word Count ---------")
        print(f"Found {number_of_words} total words")
        print("------ Character Count ------")
        for dict in sorted_dict:
                print(f"{dict["char"]}: {dict["count"]}")
        print("----------- END ------------ ")
main()