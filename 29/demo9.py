def main():
    students = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]  # Step 1: list of tuples
    averages = {}                                             # Step 2: empty dictionary

    for name, marks in students:                               # Step 3: unpack tuple
        avg = sum(marks) / len(marks)                         # Step 4: calculate average
        averages[name.lower()] = round(avg, 2)                # Step 5: lowercase name, round average to 2 decimals

    print("Student Average Score:", averages)                 # Step 6: print result

if __name__ == "__main__":
    main()