# Problem Statement
# You are given a list of tuples (product_name, price_in_dollars).
# Convert prices to INR (1 USD = 83 INR) and return only products costing more than ₹3000.

# Input

# products = [
#     ("Pen", 10),
#     ("Bag", 50),
#     ("Shoes", 60)
# ]


# Output

# [("Bag", 4150), ("Shoes", 4980)]


def demo():
        products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]
    
        price = list(map(get_price , products))
        print(price)
        
        inrprice = list(map(inr_price , price))
        print(inrprice)
def get_price(product):
    for i in product:
        return product[1]
def inr_price(price):
    for i in price:
        return price * 83

def main():
    demo()
    
if __name__ == "__main__":
    main()