# Ticket booking system

print("Welcome to the Ticket Booking System!")
ticket = input("Enter 'yes' to start or 'no' to exit: ")

# Main loop: keeps running unless user types "no"
while ticket != "no":
    if ticket == "yes":
        print("\nMain Menu:")  # \n = new line before this text (for clearer formatting)
        print("1. Buy tickets")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- Ticket Purchase ---")  # \n adds a blank line before this section

            # Show ticket categories
            print("Available categories:")
            print("1. VIP - $200")
            print("2. Premium - $150")
            print("3. Standard - $100")

            # Ask for category
            category = input("Choose a category (vip/premium/standard): ").lower()

            # Use if/elif to set the correct price based on the category
            if category == "vip":
                price = 200
            elif category == "premium":
                price = 150
            elif category == "standard":
                price = 100
            else:
                print("Invalid category. Returning to main menu.")
                continue  # This skips the rest of this loop and goes back to start

            # Handle errors if user types letters instead of numbers
            try:
                quantity = int(input("Enter the number of tickets (max 20): "))
                if quantity > 20 or quantity <= 0:
                    print("Invalid number of tickets.")
                    continue  # Go back to the start of the loop
            except ValueError:
                # This runs if the user didn't enter a number (e.g. typed "five")
                print("Please enter a valid number.")
                continue

            # Use a for loop to show each ticket reserved
            for i in range(1, quantity + 1):  # Loop from 1 to quantity
                print(f"Ticket #{i} reserved.")  # f-string: allows putting variable i inside text

            # Apply discount if more than 15 tickets
            if quantity > 15:
                print("You qualify for a 10% discount!")
                total_price = quantity * price * 0.9  # 10% off
            else:
                total_price = quantity * price

            print(f"Total price: ${total_price}")  # f-string shows total_price in the message

            # Ask how the user wants to get their tickets
            delivery = input("Delivery method (delivery/on-site): ").lower()

            if delivery == "delivery":
                if quantity < 10:
                    print("A $20 delivery fee applies.")
                    total_price += 20  # Add 20 to total price
                else:
                    print("Free delivery for large orders.")
            elif delivery == "on-site":
                print("You will collect your tickets at the venue.")
            else:
                print("Invalid delivery method. Defaulting to on-site pickup.")

            # Confirm the purchase
            confirm = input(f"Confirm purchase of {quantity} {category} ticket(s) for ${total_price}? (yes/no): ").lower()
            if confirm == "yes":
                # Ask for name and email to complete order
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                print(f"Thank you, {name}! A confirmation email will be sent to {email}.")
            else:
                print("Purchase cancelled.")

        elif choice == "2":
            # Exit option
            print("Thank you for visiting the ticket system. Goodbye!")
            break  # Break ends the while loop
        else:
            print("Invalid menu choice.")  # If user types something other than 1 or 2
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")  # If the user entered something like "maybe"

    # Ask if the user wants to continue again (this keeps the loop going)
    ticket = input("\nDo you want to continue? Enter 'yes' to continue or 'no' to exit: ")
