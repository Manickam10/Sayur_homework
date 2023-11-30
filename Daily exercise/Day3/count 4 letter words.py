"""
Problem #3
From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
for each word. Write this information at the end of file under the heading "Summary of 4 letter words"

"""
try:
    with open('Daily exercise\Day3\File1_copy.txt', 'r+') as file:
        # Read the content
        content = file.read()

        # Split the content into words
        words = content.lower().split()

        # Initialize a dictionary to store the count of each 4-letter word
        Four_letter_word_counts = {}

        # LOOp through words to count occurrences of 4-letter words
        for word in words:
            if len(word) == 4:
                if word in Four_letter_word_counts:
                    Four_letter_word_counts[word] += 1
                else:
                    Four_letter_word_counts[word] = 1

    
        # Write the summary at the end of the file
        file.write("\n\nSummary of 4 letter words:\n")
        for word, count in Four_letter_word_counts.items():
            file.write(f"{word}: {count} occurrences\n")

        print("Summary has been written to the file.")

except FileNotFoundError:
    print("Error: File does not exist.")

