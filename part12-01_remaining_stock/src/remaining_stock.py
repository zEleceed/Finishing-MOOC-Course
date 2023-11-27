def sort_by_remaining_stock(items: list):
    def stock(item):
        return item[1]

    return sorted(items, key=stock)


products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")
