import sys

from stats import get_num_words
from stats import get_char_count
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    # bookpath = "books/frankenstein.txt"
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    print(f"Analyzing book found at {bookpath}...")
    num_words = get_num_words(text)
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    counts = get_char_count(text)
    sorted_chars = chars_dict_to_sorted_list(counts)
    print(f"--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item ["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print(f"============= END ===============")
    

# print(sys.argv)
# print(sys.argv[0])

    


       

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    

    
if __name__ == "__main__":
    main()