transactions = [
    ("T101", 100),
    ("T102", 500),
    ("T101", 100),
    ("T103", 2000)
]

for transaction in transactions:
    transaction_id = transaction[0]
    amount = transaction[1]

    if amount > 1000:
        print(transaction_id, "has a large amount")

    for other in transactions:
        if transaction != other and transaction_id == other[0]:
            print(transaction_id, "is repeated")
            break
