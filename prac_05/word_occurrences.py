"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30 minutes
Actual:   27 minutes
"""


def main():
    text = input("Text: ")
    word_counts = count_words(text)
    print_sorted_word_counts(word_counts)


def count_words(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def print_sorted_word_counts(word_counts):
    sorted_words = sorted(word_counts.keys())
    max_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")


main()
