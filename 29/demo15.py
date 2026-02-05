def main():
    dicts = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
    merged = {}

    for d in dicts:
        for key, value in d.items():
            merged[key] = merged.get(key, 0) + value

    print("Dictionary Value Merger:", merged)

if __name__ == "__main__":
    main()
