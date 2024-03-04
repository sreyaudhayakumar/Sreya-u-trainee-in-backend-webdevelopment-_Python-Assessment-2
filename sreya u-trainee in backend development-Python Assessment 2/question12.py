"""12. Write a function that takes a sentence as input and returns a new sentence
with the words reversed, while keeping the order of the words in the
sentence."""

def reversed_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
output = reversed_words(input_sentence)
print("Reversed sentence is:", output)
