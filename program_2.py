#Word Separator Joseph Rydberg 10/21/2024

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""

    for s, words in enumerate(sentence):
        if s == 0:
            new_sentence += words.upper()
        if words.isupper() and s != 0:
            new_sentence += " " + words.lower()
        elif s != 0:
            new_sentence += words.lower()


    return new_sentence

# Example usage

sentence = input("Enter run on sentence with all words starting with an uppercase letter")

new_sentence = word_separator(sentence)

print(new_sentence)