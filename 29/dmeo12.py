def main():
    data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    unique_values = set()  # Use set to store unique values

    for values in data.values():
        unique_values.update(values)  # Add all values from each list

    result = sorted(unique_values)    # Sort the unique values
    print("Unique Values Extractor:", result)

if __name__ == "__main__":
    main()
