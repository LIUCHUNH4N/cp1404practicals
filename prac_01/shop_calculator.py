DISCOUNT = 0.1
total_price = 0
items_number = int(input("Number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))
for i in range(1, items_number + 1):
    item_price = float(input("Price of item: "))
    while item_price < 0:
        print("Invalid price of the item!")
        item_price = float(input("Price of item: "))
    total_price += item_price
total_price_with_discount = total_price * (1 - DISCOUNT)
print(f"Total price for {items_number} items is ${total_price_with_discount:.2f}.")

