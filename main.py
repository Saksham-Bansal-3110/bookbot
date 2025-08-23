import sys
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import os
from stats import num_words 
from stats import char_count
from stats import char_report

def get_book_text(filepath: str) -> str:
    
    if filepath.endswith(".txt"):
        with open(filepath) as f:
            return f.read()
        
    elif filepath.endswith(".epub"):
        book = epub.read_epub(filepath)
        text = []
        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_body_content(),"html.parser")
                text.append(soup.get_text())
        return "\n".join(text)
    
    else:
        raise ValueError("Unsupported file type. Use .txt or .epub")
    
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