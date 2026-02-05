def main():
    tuples_list = [(1, 5), (3, 4), (5, 6)]  # Step 1: list of tuples
    sums = []                                 # Step 2: empty list to store sums

    for a, b in tuples_list:                  # Step 3: unpack each tuple into a and b
        sums.append(a + b)                    # Step 4: calculate sum and append to list

    print("Sum of Tuples:", sums)            # Step 5: print result

if __name__ == "__main__":
    main()
