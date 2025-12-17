# 📚 BookBot

BookBot is a simple Python command-line tool that analyzes books in **.txt** and **.epub** formats.  
It reports the total word count and a frequency breakdown of alphabetic characters.

This project is intended as a learning exercise in file handling, text processing, and CLI programs.

---

## 🚀 Features

- Supports **.txt** and **.epub** files
- Counts total words in a book
- Counts how often each letter appears
- Clean and readable command-line output

---

## 🛠 Requirements

- Python **3.8+**
- Dependencies:
  - `ebooklib`
  - `beautifulsoup4`

Install dependencies with:

```bash
pip install ebooklib beautifulsoup4
````

---

## 📂 Project Structure

```text
.
├── main.py
├── stats.py
├── README.md
```

> `stats.py` must contain the following functions:
>
> * `num_words(text)`
> * `char_count(text)`
> * `char_report(char_dict)`

---

## ▶️ Usage

Run BookBot from the command line:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.epub
```

---

## 📖 Supported File Types

* `.txt` — plain text files
* `.epub` — EPUB ebooks (HTML content is automatically parsed)

Unsupported file types will raise an error.

---

## 🧠 How It Works

1. Detects the file type (`.txt` or `.epub`)
2. Extracts readable text from the book
3. Counts total words
4. Counts the frequency of each alphabetic character
5. Prints a formatted report to the terminal

---

## 📜 License

Free to use for learning and experimentation.
