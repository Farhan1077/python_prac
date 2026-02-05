def main():
    sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]  # Input list of tuples
    total_sales = {}

    # Sum quantities for each product
    for product, quantity in sales:
        total_sales[product] = total_sales.get(product, 0) + quantity

    # Find product with max sales
    highest_product = max(total_sales, key=total_sales.get)

    print("Highest Selling Product:", highest_product)

if __name__ == "__main__":
    main()
