from stats import get_num_words
from stats import get_char_cnt
from stats import sorted_dict_lst
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    # file paths
    _, path = sys.argv
    
    # text
    book = get_book_text(path)
   
    # word count
    book_wrd_cnt = get_num_words(book)
    
    # char frequency
    book_char_cnt = get_char_cnt(book)
    
    # ordered frequency list
    book_ord_char_lst = sorted_dict_lst(book_char_cnt)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wrd_cnt} total words")
    print("--------- Character Count -------")
    for dic in book_ord_char_lst:
        print(f"{dic['name']}: {dic['num']}")
    print("============= END ===============")

def get_book_text(file_path):
    '''
        Reads file path and outputs,
        file content as a string
    '''  
    with open(file_path) as f:
        # reads the contents of a file into a string
        file_contents = f.read()
        return file_contents
main()
