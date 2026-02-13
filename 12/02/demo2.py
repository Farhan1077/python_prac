def UsingMap():
    employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]
    
    for i in employees:
        Removed_emp = list(filter(min, i))
        print(Removed_emp)

def main():
    UsingMap()

if __name__ == "__main__":
    main()