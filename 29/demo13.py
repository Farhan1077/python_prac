def main():
    attendance = {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
    percentages = {}

    for name, records in attendance.items():
        total_days = len(records)
        present_days = records.count("P")
        percent = (present_days / total_days) * 100
        percentages[name] = round(percent, 2)

    print("Attendance Percentage:", percentages)

if __name__ == "__main__":
    main()
