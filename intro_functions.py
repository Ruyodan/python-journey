# # define a functions for a personal info new custommer
# def person_info(name, age, nationality):
#     print("Welcome", name)
#     print("You have", age, "years old")
#     print("You are",nationality, "by origin")
    
# number = int(input("type a number: "))
# for i in range(number):
#     name = input("Enter your first name: ").capitalize()  # Capitalize the first letter of the name
#     age = int(input("Enter your age: "))
#     nationality = input("Enter your nationality: ").capitalize() 
#     person_info(name, age, nationality)  # Call the function with the user's info



# # Define a function to calculate the total points from game scores
# def total_points():
#     points = 0  # Initialize total points to 0

#     # Keep looping to ask the user for a game score until they enter 0
#     while True:
#         game_scores = int(input("Enter the game score (0 to stop): "))  # Ask user for input

#         if game_scores == 0:
#             break  # Exit the loop if the user enters 0

#         # If score is between 5 and 10 (inclusive), add 2 points
#         if 5 <= game_scores <= 10:
#             points += 2

#         # If score is between 11 and 20 (inclusive), add 3 points
#         elif 11 <= game_scores <= 20:
#             points += 3

#         # If it's outside these ranges, add 0 points (nothing happens)

#     return points  # Return the total points after loop ends

# # Call the function and store the result in a variable
# game_points = total_points()

# # Print the final total points
# print("Total points:", game_points)


# Define a function to know the deal wanted by the user
def good_deal(cost):  
    if cost >= 50 and cost < 100:
        response = "This is a good deal!"
    elif cost >= 150:
        response = "This is an expensive deal!"
    else:
        response = "Cheap deal!"
    return response  # Return the response based on the cost of the deal

store = input("Enter the store name: ").capitalize()  # Capitalize the first letter of the store name
cost = int(input("Item cost: "))  # Get the cost of
res = good_deal(cost)  # Call the function to get the deal response
print(store, ":", res)  # Print the store name and the deal response
if res == "This is a good deal!":
    print("You can buy it now before too late!")  # If it's a good deal, suggest buying it

