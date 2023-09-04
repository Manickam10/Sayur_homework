def count_words(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Create an empty dictionary to store the word counts
    word_counts = {}

    # Iterate through each word in the sentence
    for word in words:
        # Remove punctuation from the word (optional, you can skip this if not needed)
        word = word.strip('.,!?:"()')

        # Convert the word to lowercase to handle case-insensitivity
        word = word.lower()

        # Increment the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Test the function
input_sentence = "The quick brown fox jumps over the lazy dog. The dog barks at the fox."
word_counts = count_words(input_sentence)
print(word_counts)
