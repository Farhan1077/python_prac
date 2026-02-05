def main():
    numbers = [1, 2, 3, 4, 5, 6]          # Step 1: input list
    even_numbers = [n for n in numbers if n % 2 == 0]  # Step 2: list comprehension to filter even numbers

    print("Even Numbers:", even_numbers)   # Step 3: print result

if __name__ == "__main__":
    main()







