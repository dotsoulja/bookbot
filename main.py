def word_count(text):
    return len(text.split())


def main():
    with open("books/Frankenstein.txt") as f: #opens the Frankenstein book
        file_contents = f.read()  #reads the contents into a string
    count = word_count(file_contents)
    print(f"The book contains {count} words")

main()



