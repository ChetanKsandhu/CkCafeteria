class CafeteriaMenu:
    def __init__(self):
        self.menu = {
            "Beverages": {
                "Soft Drinks": {"Cola": 2.50, "Diet Cola": 2.50, "Lemon-Lime Soda": 2.50},
                "Juices": {"Orange Juice": 3.00, "Apple Juice": 3.00},
                "Coffee": {"Drip Coffee": 1.50, "Espresso": 2.00},
            },
            "Breakfast": {
                "Egg Dishes": {"Scrambled Eggs": 2.50, "Omelette": 3.50},
                "Pancakes": {"Buttermilk Pancakes": 3.00, "Blueberry Pancakes": 3.50},
            },
            "Lunch": {
                "Sandwiches": {"Turkey Sandwich": 5.00, "Veggie Sandwich": 4.50},
                "Soups": {"Chicken Soup": 3.50, "Vegetable Soup": 3.00},
            },
        }
        self.order = {}

    def display_menu(self):
        print("\nCAFETERIA MENU")
        print("=" * 30)
        for category, subcategories in self.menu.items():
            print(f"\n{category.upper()}")
            for subcategory, items in subcategories.items():
                print(f"  {subcategory}:")
                for item, price in items.items():
                    print(f"    {item}: ${price:.2f}")

    def take_order(self):
        while True:
            category = input("\nEnter a category (or type 'done' to finish): ").title()
            if category == "Done":
                break

            if category in self.menu:
                print(f"\nAvailable subcategories in {category}:")
                for subcategory in self.menu[category]:
                    print(f"  {subcategory}")
                subcategory = input("Enter a subcategory: ").title()

                if subcategory in self.menu[category]:
                    print(f"\nItems in {subcategory}:")
                    for item, price in self.menu[category][subcategory].items():
                        print(f"  {item}: ${price:.2f}")
                    item = input("Enter the item you want to order: ").title()

                    if item in self.menu[category][subcategory]:
                        try:
                            quantity = int(input(f"How many {item}(s) would you like to order? "))
                            if item in self.order:
                                self.order[item]["quantity"] += quantity
                            else:
                                self.order[item] = {
                                    "price": self.menu[category][subcategory][item],
                                    "quantity": quantity,
                                }
                            print(f"{quantity} x {item} added to your order.")
                        except ValueError:
                            print("Invalid quantity. Please enter a number.")
                    else:
                        print("Invalid item. Please try again.")
                else:
                    print("Invalid subcategory. Please try again.")
            else:
                print("Invalid category. Please try again.")

    def display_order(self):
        print("\nYOUR ORDER")
        print("=" * 30)
        if not self.order:
            print("You haven't ordered anything yet.")
        else:
            total = 0
            for item, details in self.order.items():
                subtotal = details["price"] * details["quantity"]
                total += subtotal
                print(f"{item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
            print(f"\nTOTAL: ${total:.2f}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Display Menu")
            print("2. Take Order")
            print("3. View Order")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.take_order()
            elif choice == "3":
                self.display_order()
            elif choice == "4":
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice. Please try again.")

cafeteria = CafeteriaMenu()
cafeteria.run()
