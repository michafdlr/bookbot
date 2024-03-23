from collections import defaultdict
def count_words(string):
    return len(string.split())

def count_letters(string):
    letter_dict = defaultdict(int)
    for l in string.lower():
        if l.isalpha():
            letter_dict[l] += 1
    return letter_dict


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as f:
        file_contents = f.read()

    print(f"--- Begin report of {file_path} ---")
    print(f"There is a total of {count_words(file_contents)} words in the document.", end="\n\n")
    for letter, count in sorted(count_letters(file_contents).items(), key=lambda x: x[1], reverse=True):
        print(f"The letter '{letter}' occurs {count} times.")
main()
