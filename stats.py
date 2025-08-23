def num_words(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict[str,int]:
    dict = {}
    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else :
            dict[char] = 1
    return dict