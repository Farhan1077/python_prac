import string

def main():
    sentence = "Python is great and Python is easy"        # Step 1: input sentence
    sentence = sentence.lower()                             # Step 2: convert to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))  # Step 3: remove punctuation
    words = sentence.split()                                # Step 4: split into words

    freq = {}                                              # Step 5: empty dictionary
    for word in words:                                     # Step 6: iterate words
        freq[word] = freq.get(word, 0) + 1                # Step 7: count frequency

    print("Word Frequency Counter:", freq)                # Step 8: print result

if __name__ == "__main__":
    main()

