import sys
from stats import num_words 
from stats import char_count
from stats import char_report

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book = sys.argv[1]
    
    print("============ BOOKBOT ============")
    text = get_book_text(book)
    print(f"Analyzing book found at {book}...")
    
    print("----------- Word Count ----------")
    words = num_words(text)
    print(f"Found {words} total words")
    
    print("--------- Character Count -------")
    dict = char_count(text)
    list = char_report(dict)
    for item in list:
        if(item['chars'].isalpha()):
            print(f"{item['chars']}: {item['num']}")
    print("============= END ===============")
    
main()