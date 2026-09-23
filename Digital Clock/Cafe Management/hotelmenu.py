# ============================================
# PyCafe - Simple cafe ordering system
# Lets a customer order up to 2 items and
# calculates the total bill
# ============================================

# --- Menu setup ---
# Dictionary mapping item name -> price (Rs)
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# --- Greet the customer and display the menu ---
print("WELCOME TO PYCAFE")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80")

# Running total for the customer's order
order_total = 0

# --- First item ---
item_1 = input("Enter the name of item you want to order=")

# Check if the item exists in the menu before adding its price
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to uour order.")
else:
    # Item not found in menu dictionary
    print(f"Ordered item {item_1} is not available yet")

# --- Optional second item ---
another_order = input("Do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")

# --- Final bill ---
print(f"The total amount of items is {order_total} to pay.")