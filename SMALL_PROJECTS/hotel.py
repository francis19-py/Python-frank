total = 0

while True:
    item = input("Item name (or 'done'): ")

    if item.lower() == "done":
        break

    price = float(input("Price: "))
    total += price

print("Total Bill:", total)
print("VAT (16%):", total * 0.16)
print("Grand Total:", total * 1.16)