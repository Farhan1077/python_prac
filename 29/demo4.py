def main():
    text = "data science is fun"   # Step 1: input string
    words = text.split()            # Step 2: split string into words
    reversed_words = words[::-1]    # Step 3: reverse the list of words

    print("Reversed Words:", reversed_words)  # Step 4: print the reversed list

if __name__ == "__main__":
    main()
