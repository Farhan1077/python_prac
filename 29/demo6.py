def main():
    strings = ["hetvi", "mehul", "modi"]   # Step 1: list of strings
    length_map = {}                     # Step 2: empty dictionary

    for s in strings:                   # Step 3: iterate through each string
        length_map[s] = len(s)          # Step 4: store string length

    print("String Length Map:", length_map)  # Step 5: print result

if __name__ == "__main__":
    main()





