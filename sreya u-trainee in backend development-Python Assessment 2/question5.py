""" 5. Implement a program that reads a text file and counts the occurrences of
each word, ignoring case sensitivity."""

def count_word_occurrences(input_text):
    word_counts = {}

    for word in input_text.split():
        word_lower = word.lower()
        if word_lower in word_counts:
            word_counts[word_lower] += 1
        else:
            word_counts[word_lower] = 1
    return word_counts

file_path = input("Enter the path to the text file: ").strip()
with open(file_path, 'r') as file:
    input_text = file.read()

word_counts = count_word_occurrences(input_text)

for word, count in word_counts.items():
    print(f"{word}: {count}")

