import sys
from stats import count_words, char_count , make_list , sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            file_text = f.read()
            return file_text
    except Exception as e:
        return e

def print_list(char_list):
    for item in char_list:
        print(f"{item['char']}: {item['count']}")

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    total_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    char_cnt = char_count(book_text)
    char_cnt_list = make_list(char_cnt)
    sorted_char_list = sort_list(char_cnt_list)

    print_list(sorted_char_list)
    
    print("============= END ===============")

main()