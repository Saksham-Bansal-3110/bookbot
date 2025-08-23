from stats import num_words 
from stats import char_count

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
def main():
    words = num_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")
    print(char_count(get_book_text("books/frankenstein.txt")))
main()