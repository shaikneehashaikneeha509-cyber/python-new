# Each tuple contains: product ID, price, stock quantity
products = (
    ("P01", 10, 5),
    ("P02", 20, 2),
    ("P03", -5, 4)
)

for product in products:
    product_id = product[0]
    price = product[1]
    stock = product[2]

    print("Product:", product_id)

    if price <= 0 or stock < 0:
        print("Invalid product record.")
    else:
        value = price * stock
        print("Inventory value:", value)

        if stock < 3:
            print("Needs replenishment.")
