# # creating a function that accepts score as a parameter :
# def evaluate_score(score): 
#     print("Your score is:", score)  # Print the score provided by the user
#     if score > 0 and score <= 50:
#         print("Below passing, Improve your grade!")
#     elif score > 50 and score <= 70:
#         print("Barely passing the class!")
#     elif score > 70 and score <= 90:
#         print("You have a passing grade!")
#     else:
#         print("You are one of the best in class!")
    
# user_score = int(input("Enter your score: "))  # Get the score from the user
# evaluate_score(user_score)  # Call the function to evaluate the score




# creating a funcion to add on extra flight charges : 
def charges(flight_cost):
    
    upgrade = input("Do you want to upgrade your flight? (yes/no): ").lower()  # Ask if the user wants an upgrade
    if upgrade == "yes":
        flight_cost += 99  # Add $99 if the user wants an upgrade
        
    baggage = input("Do you have baggage? (yes/no): ").lower()  # Ask if the user has baggage      
    if baggage == "yes":
        flight_cost += 35  # Add $35 if the user has baggage
        
    tax = (flight_cost * 0.08) + flight_cost  # Calculate 8% tax on the flight cost
    return tax # Return the total cost including tax

price = int(input("Enter the flight cost: "))  # Get the flight cost from the user
grand_total = charges(price)  # Call the function to calculate total cost
print("The total cost of your flight is: $", grand_total)  # Print the total cost including tax