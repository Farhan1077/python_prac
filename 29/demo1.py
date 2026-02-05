def main():
    numbers = [1, 2, 2, 3, 3, 3]
    count_dict = {}

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    print(count_dict)


if __name__ == "__main__":
    main()
