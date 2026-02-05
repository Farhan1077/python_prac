def main():
    text = "banana"
    index_map = {}

    for idx, char in enumerate(text):
        if char not in index_map:
            index_map[char] = []
        index_map[char].append(idx)

    # Convert lists to tuples
    for char in index_map:
        index_map[char] = tuple(index_map[char])

    print("Character Index Map:", index_map)

if __name__ == "__main__":
    main()
