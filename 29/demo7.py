def main():
    text = "programming"               # Step 1: input string
    unique_chars = []                   # Step 2: list to store unique characters

    for char in text:                   # Step 3: iterate each character
        if char not in unique_chars:    # Step 4: check if it's not already added
            unique_chars.append(char)   # Step 5: add to the list

    print("Unique Characters:", tuple(unique_chars))  # Step 6: convert to tuple and print

if __name__ == "__main__":
    main()
