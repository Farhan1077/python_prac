def costom():
    customers = [
        {"name": "A", "purchases": [50, 200, 300], "active": True},
        {"name": "B", "purchases": [500, 20], "active": False},
        {"name": "C", "purchases": [150, 250], "active": True}
    ]
    
    cust = list(filter(lambda c: c["active"], customers))
    total = 0
    for c in cust:
        validpr = list(filter(lambda a: a > 100, c["purchases"]))
        valid = list(map(lambda p: p * 1.10, validpr))
        
        total += sum(valid)
    print(total)
    
def disc():
    products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
    validpro = list(filter(lambda p : p[1] == "Electronics", products))
    total = 0
    for c in validpro:
        total += c[2] * 0.8
        
    print(total)   
        
def scorecalc():
    students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]
    
    std = list(filter(lambda f : sum(f["marks"])/len(f["marks"])>= 60, students))
    print(std)
    total = 0
    for s in std:
        grace = list(map(lambda x: x+ 5 , s["marks"]))
        total = sum(grace)
    print(total)
def main():
    #costom()
    #disc()
    scorecalc()
if __name__ == "__main__":
    main()
