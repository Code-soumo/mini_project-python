# Define the restaurant menu
menu = {
    'pizza': 350,
    'pasta': 155,
    'burger': 100,
    'salad': 150,
    'coffee': 265
}

# Greeting
print("WELCOME TO OUR CACTUS RESTAURANT")
print("This is Our Menu")
print("Pizza: Rs-350\nPasta: Rs-155\nBurger: Rs-100\nSalad: Rs-150\nCoffee: Rs-265\n")

order_total = 0

item_1 = input("Enter the name of the food you want to order: ").lower()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order")
else:
    print(f"Sorry, '{item_1}' is not available!")

# Ask for another item
another_order = input("Do you want to add another item? (yes/no): ").lower()

if another_order == "yes":
    item_2 = input("Enter your second food: ").lower()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order")
    else:
        print(f"Sorry, '{item_2}' is not available!")


print(f"\nTotal amount to pay is Rs {order_total}")
print("Thank you for your order!")